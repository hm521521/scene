from django.urls import path
from . import manage_users, artdata, indicator, IP, scores, analyze, cameras

urlpatterns=[
    path('manage_users/', manage_users.dispatcher),
    path('artdata/', artdata.dispatcher),
    path('indicator/', indicator.dispatcher),
    path('IP/', IP.dispatcher),
    path('scores/', scores.dispatcher),
    path('analyze/', analyze.dispatcher),
    path('cameras/', cameras.dispatcher),

]