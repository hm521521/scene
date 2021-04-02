from django.http import HttpResponse
# from lib.handler import dispatcherBase



def super_group(request):
    return HttpResponse("返回人群组成员数量")

