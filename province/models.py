from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.

class Province(Document):
    name = StringField()
    description = StringField()
    country = StringField()
