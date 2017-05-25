from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField("name",max_length=20) #user name
    password = models.CharField("pass",max_length=20) #pass
    realname = models.TextField()
    email = models.EmailField("email",blank=True)
    def __str__(self):
        return '%s'%(self.username)




class Classfication(models.Model):
    classid = models.AutoField(primary_key=True)
    classname = models.CharField("name",max_length=30)
    def __str__(self):
        return '%s' % (self.name)


class article(models.Model):
     articleid = models.AutoField(primary_key=True)
     user = models.ForeignKey(Users)
     content = models.TextField()
     smallcontent = models.TextField()
     title = models.TextField()

class commnent(models.Model):
     commnentid = models.AutoField(primary_key=True)
     articleid = models.IntegerField()
     commnenttext = models.TextField()
     user = models.ForeignKey(Users)

