from django.http import HttpResponse
# from lib.handler import dispatcherBase



def ass_dyn(request):
    return HttpResponse("动态亮度")