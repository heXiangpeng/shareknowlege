# -*- coding:utf-8 -*-

import models
from django.http import HttpResponse

class ServiceApi:
    name=""
    password=""

    def login(self,name,password):
        self.name=name
        self.password=password
        user = models.Users.objects.filter(username__exact=name,password__exact=password)
        if user:
            return user[0]
        else:
            return ''





    def regiser(self,name,password,realname,email):
        self.name = name
        self.password =password
        userregister = models.Users()
        userregister.username=name
        userregister.password=password
        userregister.realname = realname
        userregister.email = email
        userregister.save()

    def __init__(self):
        print ""






