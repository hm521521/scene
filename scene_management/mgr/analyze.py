from django.http import HttpResponse
from lib.handler import dispatcherBase



def list_anlyze(request):
    return HttpResponse("列出分析")

def del_anlyze(request):
    return HttpResponse("删除分析")

Action2Handler = {
    'list_anlyze': list_anlyze,
    'del_anlyze': del_anlyze,
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)