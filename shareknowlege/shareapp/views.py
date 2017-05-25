# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import sys
from ServiceApi import *

import models

reload(sys)


sys.setdefaultencoding('utf-8')

api = ServiceApi()



# 删除账号
def usernamedelete(request):
    context = {}
    name = request.session.get('name', default='')
    if name != '':
        if request.GET:
            id = request.GET['name']
            models.Users.objects.filter(userid__exact=id).delete()
            return HttpResponseRedirect('/adminhome')

    else:
        return HttpResponseRedirect('/login')


def homesearch(request):
    return render(request, 'homesearch1.html')



def index(request):

    context = {}
    name = request.session.get('name', default='')
    if name!='':
       arcticle = models.article.objects.all().reverse()
       context['username'] = name
       context['arcticle'] = arcticle
    #return HttpResponse("succsess"+str(arcticle))
       return render(request, 'index.html',context)
    else:
       return HttpResponseRedirect('/login')



# 登陆账号
def login(request):
    if request.POST:
        name = request.POST['username']  #接收请求
        password = request.POST['password']
        user = api.login(name,password)
        if name=='admin' and password=='admin':
            request.session['name'] = 'admin'

            context = {}
            arcticle = models.article.objects.all() #取出所有数据
            user = models.Users.objects.all()
            context['username'] = name
            context['arcticle'] = arcticle
            context['user'] = user
            # return HttpResponse("succsess"+str(arcticle))
            return render(request, 'admin.html', context)  #渲染界面

        if user != '':
           request.session['name'] = name
           context = {}
           context['username'] = user.username
           return HttpResponseRedirect('/index')  #返回首页

    return render(request,'login.html')

def register(request):
    if request.POST:
        name = request.POST['username']
        password = request.POST['password']
        realname = request.POST['realname']
        verificationpass = request.POST['verificationpass']
        if password==verificationpass:
            api.regiser(name,password,realname,"")
            request.session['name'] = name
            return HttpResponseRedirect("/index")

    return render(request, 'register.html')


# 管理员操作
@csrf_exempt
def admin(request):
    context = {}
    name = request.session.get('name', default='')
    if name != '':
        arcticle = models.article.objects.all()
        user = models.Users.objects.all()
        context['username'] = name
        context['arcticle'] = arcticle
        context['user'] = user
        # return HttpResponse("succsess"+str(arcticle))
        return render(request, 'admin.html', context)
    else:
        return HttpResponseRedirect('/index')



def editor(request):
    name = request.session.get('name', default='')
    if name != '':
       return render(request,"editor.html")
    else:
       return HttpResponseRedirect("/login")  #页面跳转


def delete(request):
    context = {}
    name = request.session.get('name', default='')
    if name != '':
        if request.GET:
            id = request.GET['id']
            models.article.objects.filter(articleid__exact=id).delete()
            return HttpResponseRedirect('/adminhome')

    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def view(request):
    context = {}
    name = request.session.get('name', default='')
    if name != '':
        if request.GET:
            id = request.GET['id']
            request.session['id'] = id
            arcticle = models.article.objects.filter(articleid__exact=id)[0]  #取出某一篇文章
            comment = models.commnent.objects.filter(articleid__exact=id)
            context['username'] = name
            context['arcticle'] = arcticle
            context['comment'] = comment
        # return HttpResponse("succsess"+str(arcticle))
        return render(request, 'events_show.html', context)
    else:
        return HttpResponseRedirect('/login')


@csrf_exempt
def logout(request):
    request.session['name'] = ''
    return HttpResponseRedirect('/login')



@csrf_exempt
def addtext(request):
    text = request.POST['text']
    title = request.POST['title']
    textsmall = request.POST['smalltext']
    name = request.session.get('name', default='')
    user = models.Users.objects.filter(username__exact=name)[0]  # 取出某一篇文章

    article = models.article()
    article.user = user
    article.content=text;
    article.smallcontent=textsmall
    article.title = title
    #user = models.Users(username=api.name, password=api.password)
    #article.users = user
    article.save()
    return HttpResponse("succsess")


@csrf_exempt
def addcomment(request):
    commenttext = request.POST['comment']
    name = request.session.get('name', default='')
    user = models.Users.objects.filter(username__exact=name)[0]  # 取出某一篇文章
    id = request.session.get('id', default=0)
    print id
    comment = models.commnent()
    comment.articleid = id
    comment.commnenttext = commenttext
    comment.user = user
    comment.save()
    return HttpResponse("succsess")







