from django.http import HttpResponse
from lib.handler import dispatcherBase



def list_artdata(request):
    return HttpResponse("列出数据")

def add_artdata(request):
    return HttpResponse("添加数据")

def modify_artdata(request):
    return HttpResponse("修改数据")

def del_artdata(request):
    return HttpResponse("删除数据")

Action2Handler = {
    'list_artdata': list_artdata,
    'add_artdata': add_artdata,
    'modify_artdata': modify_artdata,
    'del_artdata':del_artdata,
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)