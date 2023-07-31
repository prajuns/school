from django.urls import path
from . import views
app_name='sclapp'

urlpatterns=[
    path('',views.home,name="home"),


]