from django.http import HttpResponse
from lib.handler import dispatcherBase



def list_users(request):
    return HttpResponse("列出用户")

def modify_users(request):
    return HttpResponse("修改用户")

def del_users(request):
    return HttpResponse("删除用户")

Action2Handler = {
    'list_users': list_users,
    'modify_users': modify_users,
    'del_users': del_users,
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)