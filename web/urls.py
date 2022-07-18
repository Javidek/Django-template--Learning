
from django.urls import path
from web.views import *


app_name = 'web'

urlpatterns = [
    path('',index_view,name='index')
]