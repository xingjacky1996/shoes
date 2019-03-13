from django.urls import path
from . import views

app_name='demo'
urlpatterns = [
    path('',views.get,name='get'),
    path('updateusershoes',views.updateusershoes,name='updateusershoes'),
    path('<id>/getusershoes',views.getusershoes,name='getusershoes'),
]