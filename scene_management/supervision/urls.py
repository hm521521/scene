from django.urls import path
from . import group, cameras,predictions,intensity,tumble,composition,distribution

urlpatterns=[
    path('group/', group.super_group),
    path('cameras/',cameras.imcamera),
    path('predicitions/', predictions.super_predict),
    path('intensity/', intensity.super_intensity),
    path('tumble',tumble.super_tumble),
    path('composition',composition.super_comp),
    path('distribution',distribution.super_distri),

]