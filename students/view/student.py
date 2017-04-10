from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models.student import Student
from ..models.group import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib import messages
from PIL import Image
from ..util import get_current_group
from django.contrib.auth.decorators import login_required



@login_required
def students_list(request):
   current_group = get_current_group(request)
   st = Student.objects.all()
   con = len(st)
   current_user=request.user.id
   if current_group:
      students = Student.objects.filter(student_group_id=current_group)
   else:   
      students = Student.objects.filter(user_s=current_user)
   # try to order students list
   order_by = request.GET.get('order_by', '')
   if order_by in ('last_name', 'first_name', 'ticket', '#'):
     students = students.order_by(order_by)
     if request.GET.get('reverse', '') == '1':
       students = students.reverse()
   # paginate students
   paginator = Paginator(students, 3)
   page = request.GET.get('page')
   try:
     students = paginator.page(page)
   except PageNotAnInteger:
   # If page is not an integer, deliver first page.
     students = paginator.page(1)
   except EmptyPage:
     # If page is out of range (e.g. 9999), deliver
     # last page of results.
     students = paginator.page(paginator.num_pages)
   return render(request, 'students/stud.html',
     {'students': students, 'con': con})







@login_required
def stud_add(request):
  current_user=request.user.id
  Groups = Group.objects.filter(user_g=current_user)
  if Groups:

    # was form posted?
    if request.method == "POST":
      # was form add button clicked?
      if request.POST.get('add_button') is not None:
        # errors collection
        errors = {}
        # data for student object
        data = {'notes': request.POST.get('notes')}
        # validate user input
        first_name = request.POST.get('first_name', '').strip()
        if not first_name:
          errors['first_name'] = _(u"First Name field is required")
        else:
          data['first_name'] = first_name
        last_name = request.POST.get('last_name', '').strip()
        if not last_name:
          errors['last_name'] = _(u"Last Name field is required")
        else:
          data['last_name'] = last_name
        birthday = request.POST.get('birthday', '').strip()
        if birthday:
          try:
            datetime.strptime(birthday, '%Y-%m-%d')
          except Exception:
            errors['birthday'] = _(u"Enter the correct date format (eg 1986-03-23")
          else:
            data['birthday'] = birthday
      
        student_group_id = request.POST.get('student_group_id', '').strip()
        if not student_group_id:
          errors['student_group_id'] = _(u"Select a class")
        else:
          groups = Group.objects.filter(pk=student_group_id)
          if len(groups) != 1:
            errors['student_group'] = _(u"Select a correct class")
          else:
            data['student_group_id'] = groups[0]
      
      
        data['user_s'] = current_user     
        # save student
        if not errors:
          student = Student(**data)
          student.save()
          # redirect to students list
          return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('main'),_(u"Pupil successfully added")))
        else:
          # render form with errors and previous user input
          return render(request, 'students/students_add_edit.html',
          {'groups': Group.objects.all().order_by('title'),'errors': errors})
      elif request.POST.get('cancel_button') is not None:
        # redirect to home page on cancel button
        return HttpResponseRedirect ( u'%s?status_message=%s'  % (reverse('main'),_(u"Adding the pupil canceled")))
    else:
     # initial form render
     return render(request, 'students/students_add_edit.html',
     {'groups': Group.objects.filter(user_g=current_user).order_by('title'), 'Groups': Groups})
  else:
    return render(request, 'students/nogroups.html', {})








@login_required
def student_edit(request, pk):
    current_user=request.user.id
    students = Student.objects.filter(pk=pk)
    groups = Group.objects.filter(user_g=current_user)

    
    if request.method == "POST":
        data = Student.objects.get(pk=pk)
        if request.POST.get('add_button') is not None:
            data.middle_name = request.POST.get('middle_name', '').strip()
            data.notes = request.POST.get('notes', '').strip()
            errors = {}

            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = _(u"Name is mandatory")
            else:
                data.first_name = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = _(u"Last name is required")
            else:
                data.last_name = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = _(u"Date of birth is mandatory")
            else:
                try:
                    bd = datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = _(u"Enter the correct date format (eg. 12/30/1987)")
                else:
                    data.birthday = bd
           
           
          

            student_group_id = request.POST.get('student_group_id', '').strip()
            if not student_group_id:
                errors['student_group_id'] = _(u"Group is mandatory")
            else:
                gr = Group.objects.filter(pk=student_group_id)
                if len(gr) != 1:
                    errors['student_group_id'] = _(u"Select the correct group")
                else:
                    grps = Group.objects.filter(leader=Student.objects.get(pk=pk))
                    if len(grps) > 0 and int(student_group_id) != grps[0].pk:
                        errors['student_group_id'] = _(u"The pupil is the head of another group")
                    else:
                        data.student_group_id = gr[0]


            data.user_s = current_user

            if errors:
                return render(request, 'students/students_add_edit.html', {'pk': pk, 'student': data, 'errors': errors, 'groups': groups})
            else:
                data.save()
                return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('main'),_(u"Edit the pupil has successfully completed")))
        elif request.POST.get('cancel_button') is not None:

            return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('main'),_(u"Editing pupil canceled")))
        
    else:
        return render(request,
                      'students/students_add_edit.html',
                      {'pk': pk, 'student': students[0], 'groups': groups})





        





@login_required
def student_delete(request, pk):
    students = Student.objects.filter(pk=pk)
    
    if request.method == "POST":
        if request.POST.get('yes') is not None:
          students.delete()
          return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('main'),_(u"Pupil successfully removed")))
        elif request.POST.get('cancel_button') is not None:
          return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('main'),_(u"Removal of the pupil canceled")))
        
    else:
        return render(request,
                      'students/students_delete.html',
                      {'pk': pk, 'student': students[0]})



