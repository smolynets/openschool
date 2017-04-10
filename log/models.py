from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class StProfile(models.Model):


  user = models.OneToOneField(User)
  class Meta(object):
    verbose_name = _(u"User Profile")

  mobile_phone = models.CharField(
    max_length=12,
    blank=True,
    verbose_name=_(u"Mobile Phone"),
  )
  lang = models.CharField(
    max_length=12,
    blank=True,
    verbose_name=_(u"lang"),
  )
  def __unicode__(self):
    return self.user.username






class logentry(models.Model):
  level = models.CharField(
    max_length=20,
    blank=False)
  asctime = models.DateTimeField(
    blank=False,
    null=True)
  module = models.CharField(
    max_length=100,
    blank=False,)
  message = models.TextField(
    blank=False,)
  def __unicode__(self):
    return u"%s %s %s %s" % (self.level, self.asctime, self.module, self.message)