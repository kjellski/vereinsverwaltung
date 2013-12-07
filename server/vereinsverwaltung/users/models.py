from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from organisations.models import Organisation
class CustomUser(AbstractBaseUser):
    first_name = models.CharField('first name', max_length=30, blank=False)
    last_name = models.CharField('last name', max_length=30, blank=False)
    organisation = models.ForeignKey(Organisation)
    objects = UserManager()
    def __unicode__(self):
        return unicode("%s %s"%(self.first_name, self.last_name))

