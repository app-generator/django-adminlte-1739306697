# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Patient(models.Model):

    #__Patient_FIELDS__
    idpatient = models.IntegerField(null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    sexe = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    #__Patient_FIELDS__END

    class Meta:
        verbose_name        = _("Patient")
        verbose_name_plural = _("Patient")


class Consultation(models.Model):

    #__Consultation_FIELDS__
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Consultation_FIELDS__END

    class Meta:
        verbose_name        = _("Consultation")
        verbose_name_plural = _("Consultation")


class Medecin(models.Model):

    #__Medecin_FIELDS__
    nom = models.CharField(max_length=255, null=True, blank=True)

    #__Medecin_FIELDS__END

    class Meta:
        verbose_name        = _("Medecin")
        verbose_name_plural = _("Medecin")



#__MODELS__END
