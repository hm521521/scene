from django.http import HttpResponse
from lib.handler import dispatcherBase



def list_IP(request):
    return HttpResponse("列出IP")

def add_IP(request):
    return HttpResponse("添加IP")

def modify_IP(request):
    return HttpResponse("修改IP")

def del_IP(request):
    return HttpResponse("删除IP")

Action2Handler = {
    'list_IP': list_IP,
    'add_IP': add_IP,
    'modify_IP': modify_IP,
    'del_IP': del_IP,
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)