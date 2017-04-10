from django.db import models

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
  user = models.TextField(
    blank=False,)
  def __unicode__(self):
    return u"%s %s %s %s" % (self.level, self.asctime, self.module, self.message)