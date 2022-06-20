#write this full****
from django.urls import path
from employee import views
urlpatterns=[
#for function
   # path("index/",views.index),
   # path("login/",views.login),

#for class

    path("index", views.indexview.as_view(),name="emp-index"),
    path("login",views.loginview.as_view(),name="login"),
    path("register",views.registrationview.as_view(),name="register"),
    path("profile/add",views.EmployeeCreateView.as_view(),name="emp-add"),


]