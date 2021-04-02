from django.urls import path
from . import functions

urlpatterns=[
    path('signin/',functions.signin),
    path('signout/',functions.signout),
    path('verify/',functions.dispatcher),

]