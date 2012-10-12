from django.db import models

# Create your models here.

class BrokenRelationKorean(models.Model):

  broken = models.TextField()
  restore = models.TextField()
  # unique id of the person connecting to the site
  remote_id = models.CharField(max_length=256)
  remote_addr = models.CharField(max_length=64)
  remote_host = models.CharField(max_length=128)
  user_agent = models.CharField(max_length=256)
  referrer = models.CharField(max_length=256, null=True, blank=True)

  timestamp = models.DateTimeField(auto_now_add=True)


class Country(models.Model):

  name = models.CharField(max_length=64)
  iso_code = models.CharField(max_length=3)

  def __unicode__(self):
    return self.name


class BrokenRelationEnglish(models.Model):

  country = models.ForeignKey(Country)
  broken = models.TextField()
  restore = models.TextField()
  # unique id of the person connecting to the site
  remote_id = models.CharField(max_length=256)
  remote_addr = models.CharField(max_length=64)
  remote_host = models.CharField(max_length=128)
  user_agent = models.CharField(max_length=256)
  referrer = models.CharField(max_length=256, null=True, blank=True)

  timestamp = models.DateTimeField(auto_now_add=True)
