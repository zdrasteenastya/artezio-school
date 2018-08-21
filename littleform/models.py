# -*- coding: utf-8 -*-

from django.db import models


class Junior(models.Model):
    username = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    link_sns = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    english = models.CharField(max_length=200)
    languages = models.TextField()
    experience = models.TextField()
    link_code = models.TextField()
    agreement = models.BooleanField(default=False)

    def __str__(self):
        return self.username.encode('utf-8')