from django.conf.urls import url
from . import views

urlpatterns = [
         url(r'^$', views.index, name='index'),
         url(r'index2', views.index2, name='index2'),
            ]
