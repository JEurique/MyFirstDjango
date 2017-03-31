from django.conf.urls import url
#from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^lista_registros/', listar_registros),
    url(r'^$', index, name='index'),
    #url(r'^lista_registros/(\d+)/$', listar_registros)
]