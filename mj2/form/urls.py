from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.index),
    path('sdata/',views.sdata),
    path('login/',views.login),
    path('table/',views.table),
    path('loginfunction/',views.ldata),
    path('updateform/<int:uid>/',views.update),
    path('updatefunction/',views.updatefunction),
    re_path(r'^delete/(?P<pk>[0-9]+)/$',views.delete,name="delete")
]
