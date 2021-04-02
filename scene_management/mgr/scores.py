from django.http import HttpResponse
from lib.handler import dispatcherBase



def list_scores(request):
    return HttpResponse("列出评分")

def del_scores(request):
    return HttpResponse("删除评分")

Action2Handler = {
    'list_scores': list_scores,
    'del_scores': del_scores,
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)