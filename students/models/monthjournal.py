from django.utils.translation import ugettext_lazy as _
from django.db import models
class MonthJournal(models.Model):
  
    class Meta:
      verbose_name = _(u'Monthly journal')
      verbose_name_plural = _(u'Monthly journals')
      
    student = models.ForeignKey('Student',
      verbose_name=_(u'Student'),
      blank=False,
      unique_for_month='date')
    date = models.DateField(
      verbose_name=_(u'Date'),
      blank=False)
    user_j = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"user"))
    
    present_day1 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day1"))

    present_day2 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day2"))

    present_day3 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day3"))

    present_day4 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day4"))

    present_day5 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day5"))

    present_day6 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day6"))

    present_day7 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day7"))

    present_day8 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day8"))

    present_day9 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day9"))

    present_day10 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day10"))

    present_day11 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day11"))

    present_day12 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day12"))

    present_day13 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day13"))

    present_day14 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day14"))

    present_day15 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day15"))

    present_day16 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day16"))

    present_day17 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day17"))

    present_day18 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day18"))

    present_day19 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day19"))

    present_day20 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day20"))

    present_day21 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day21"))

    present_day22 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day22"))

    present_day23 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day23"))

    present_day24 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day24"))

    present_day25 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day25"))

    present_day26 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day26"))

    present_day27 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day27"))

    present_day28 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day28"))

    present_day29 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day29"))

    present_day30 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day30"))

    present_day31 = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"present_day31"))

    
   
    def __unicode__(self):
      return u'%s: %d, %d' % (self.student.last_name, self.date.month,
        self.date.year)














