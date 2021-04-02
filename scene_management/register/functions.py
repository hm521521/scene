from django.shortcuts import render
from django.http import HttpResponse
from lib.handler import dispatcherBase

def signin(request):
    return HttpResponse("下面是登录的信息")

def signout(request):
    return HttpResponse("下面是退出的信息")





def verify_picture(request):
    return HttpResponse("获取验证码")

def verify_count(request):
    return HttpResponse("获取手机验证码")

def verify_user(request):
    return HttpResponse("用户注册")

Action2Handler = {
    'verify_picture': verify_picture,
    'verify_count': verify_count,
    'verify_user': verify_user,
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)