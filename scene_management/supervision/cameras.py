from django.http import HttpResponse
# from lib.handler import dispatcherBase



def imcamera(request):
    return HttpResponse("接入摄像头")