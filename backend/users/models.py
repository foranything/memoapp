from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.urlresolvers import reverse
from django.urls import reverse
# Create your models here.


class User(AbstractUser):

    # GENDER_CHOICES = (
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    #     ('not-specified', 'Not specified')
    # )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    # username = models.CharField(max_length=25, default="")
    # name = models.CharField(('Name of User'), blank=True, max_length=255)
    # website = models.URLField(null=True)
    # bio = models.TextField(null=True)
    # phone = models.CharField(max_length=140, null=True)
    # gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

