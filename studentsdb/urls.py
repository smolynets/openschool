"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include,url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from students.view.journal import JournalView
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView, TemplateView
from students.view.student import stud_add, student_edit, student_delete
from students.view.group import groups_add, groups_edit, groups_delete 
from students.view.logs import logs
from students.view.contact_admin import contact_admin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from registration.backends.default import views as registration_views
from log.views import user_edit





js_info_dict = {
'packages': ('students',),
}

urlpatterns = patterns('',
	#journal
url(r'^(?P<pk>\d+)?/?$', login_required(JournalView.as_view()), name='journal'),
# Students urls
url(r'^pupils$', 'students.view.student.students_list', name='main'),
url(r'^pupil_add$', login_required(stud_add), name='s_add'),
url(r'^pupil/(?P<pk>\d+)/edit/$',login_required(student_edit),
name='students_edit'),
url(r'^pupil/(?P<pk>\d+)/delete/$', login_required(student_delete),name='students_delete'),
#Groups urls
url(r'^classes$', 'students.view.group.grup', name='groups'),
url(r'^class_add$', 'students.view.group.groups_add', name='groups_add'),
url(r'^class/(?P<pk>\d+)/edit/$',
'students.view.group.groups_edit', name='groups_edit'),
url(r'^class/(?P<pk>\d+)/delete/$',
'students.view.group.groups_delete', name='groups_delete'),
url(r'^class/(?P<pk>\d+)/one/$',
'students.view.group.groups_one', name='groups_one'),
url(r'^admin/', include(admin.site.urls)),

#logs
url(r'^logs$', login_required(logs), name='logs'),
# Contact Admin Form
url(r'^contact-admin/$', login_required(contact_admin),
name='contact_admin'),
#i18n of js
url(r'^jsi18n.js$', 'django.views.i18n.javascript_catalog', js_info_dict),

# User Related urls
url(r'^users/profile/$', login_required(TemplateView.as_view(
template_name='registration/profile.html')), name='profile'),
url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'main'}, name='auth_logout'),
url(r'^register/complete/$', TemplateView.as_view(template_name='registration/confirm_email.html'), name='registration_complete'),
url(r'^users/', include('registration.backends.default.urls', namespace='users')),
url(r'^users/activate/(?P<activation_key>\w+)/$', registration_views.ActivationView.as_view(),
name='registration_activate'),
url(r'^users/activate/complete/$',
TemplateView.as_view(template_name='registration/activation_complete.html'),
name='registration_activation_complete'),
url(r'^users_list$', 'log.views.users_list', name='users_list'),
url(r'^users/(?P<pk>\d+)/one/$',
'log.views.users_one', name='users_one'),
url(r'^prof/(?P<pk>\d+)/edit$', 'log.views.user_edit', name='prof_edit'),
url(r'^user/(?P<pk>\d+)/edit$', 'log.views.user_one_edit', name='user_edit'),
url(r'^activate/complete/$', TemplateView.as_view(template_name='registration/login.html'),
    name='registration_activation_complete'),


url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),


# Social Auth Related urls
url('^social/', include('social.apps.django_app.urls', namespace ='social')),
)

if DEBUG:
 # serve files from media folder
 urlpatterns += patterns('',
 url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
 'document_root': MEDIA_ROOT}))
