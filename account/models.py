from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    dob = models.DateField()
    gender = models.CharField(max_length=1)

    def __unicode__(self):
        u"%s" % self.user


# Create your models here.
