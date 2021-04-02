from django.http import HttpResponse
# from lib.handler import dispatcherBase



def super_comp(request):
    return HttpResponse("返回人群组成")