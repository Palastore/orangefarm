from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from mongoengine.django.auth import User as MongoUser
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login
import requests
import uuid
import cookielib
import urllib2
import Cookie
from user_profile.models import *

# Create your views here.

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        template = loader.get_template('notlogin.html')
        return HttpResponse(template.render({}, request))
    template = loader.get_template('logout/index.html')
    return HttpResponse(template.render({'foo': 'bar'}, request))
