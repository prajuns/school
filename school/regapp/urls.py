from django.urls import path
from . import views
app_name="regapp"

urlpatterns=[
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('formbutton',views.formbutton,name="formbutton"),
    path('form',views.form,name="form"),





]