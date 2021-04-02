from django.urls import path
from . import sta_bright, chroma, dyn_bright, IP, scores


urlpatterns=[
    path('sta_bright/', sta_bright.ass_sta),
    path('chroma/', chroma.ass_chr),
    path('dyn_bright/', dyn_bright.ass_dyn),
    path('IP/', IP.ass_IP),
    path('scores', scores.ass_sco),

]