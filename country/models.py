from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.

class Country(Document):
    name = StringField()
    description = StringField()
