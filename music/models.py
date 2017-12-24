from __future__ import unicode_literals

from django.db import models

# Create your models here.
class input(models.Model):
    visitorControl = models.IntegerField(max_length=20)
    visitorVariation = models.IntegerField(max_length=20)
    conversionControl = models.IntegerField(max_length=20)
    conversionVariation = models.IntegerField(max_length=20)