from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
# from mysite.core import views as core_views
app_name='index'
urlpatterns = [
    path('', views.index, name="index" ),

]

