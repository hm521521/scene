from django.http import HttpResponse
from lib.handler import dispatcherBase



def list_cameras(request):
    return HttpResponse("列出摄像头")

def del_cameras(request):
    return HttpResponse("删除摄像头")

Action2Handler = {
    'list_cameras': list_cameras,
    'del_cameras': del_cameras,
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)