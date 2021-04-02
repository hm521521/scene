from django.http import HttpResponse
from lib.handler import dispatcherBase


def list_indicator(request):
    return HttpResponse("列出指标")


def add_indicator(request):
    return HttpResponse("添加指标")


def modify_indicator(request):
    return HttpResponse("修改指标")


def del_indicator(request):
    return HttpResponse("删除指标")


def list_sta_bright(request):
    return HttpResponse("列出静态亮度指标")


def add_sta_bright(request):
    return HttpResponse("添加静态亮度指标")


def modify_sta_bright(request):
    return HttpResponse("修改静态亮度指标")


def del_sta_bright(request):
    return HttpResponse("删除静态亮度指标")


def list_dyn_bright(request):
    return HttpResponse("列出动态亮度指标")


def add_dyn_bright(request):
    return HttpResponse("添加动态亮度指标")


def modify_dyn_bright(request):
    return HttpResponse("修改动态亮度指标")


def del_dyn_bright(request):
    return HttpResponse("删除动态亮度指标")


def list_chroma(request):
    return HttpResponse("列出彩度")


def add_chroma(request):
    return HttpResponse("添加彩度")


def modify_chroma(request):
    return HttpResponse("修改彩度")


def del_chroma(request):
    return HttpResponse("删除彩度")


Action2Handler = {
    'list_indicator': list_indicator,
    'add_indicator': add_indicator,
    'modify_indicator': modify_indicator,
    'del_indicator': del_indicator,
    'list_sta_bright': list_sta_bright,
    'add_sta_bright': add_sta_bright,
    'modify_sta_bright': modify_sta_bright,
    'del_sta_bright': del_dyn_bright,
    'list_dyn_bright': list_dyn_bright,
    'add_dyn_bright': add_dyn_bright,
    'modify_dyn_bright': modify_dyn_bright,
    'del_dyn_bright': del_dyn_bright,
    'list_chroma': list_chroma,
    'add_chroma': add_chroma,
    'modify_chroma': modify_chroma,
    'del_chroma': del_chroma,
}


def dispatcher(request):
    return dispatcherBase(request, Action2Handler)
