# #write this full****
 #from django.urls import path
# from employee import views
# urlpatterns=[
# #for function
#    # path("index/",views.index),
#    # path("login/",views.login),
#
# #for class
#
#     path("index", views.indexview.as_view(),name="emp-index"),
#     path("login",views.loginview.as_view(),name="login"),
#     path("register",views.registrationview.as_view(),name="register"),
#     path("profile/add",views.EmployeeCreateView.as_view(),name="emp-add"),
#
#
# ]

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from employee import views


urlpatterns=[
     path("add",views.EmployeeCreateView.as_view(),name="add-emp"),
     path("all",views.EmployeeListView.as_view(),name="emp-list"),
     path("detail/<str:e_id>",views.EmployeeDetailView.as_view(),name="emp-detail"),
     path("change/<str:e_id>",views.EmployeeEditView.as_view(),name="emp-edit"),
     path("remove/<str:e_id>",views.remove_employee,name="emp-remove"),
     path("",views.index,name="index"),
     path("accounts/signup",views.SignUpView.as_view(),name="sign-up"),
     path("accounts/signin",views.LoginView.as_view(),name="signin"),
     path("accounts/signout", views.sign_out,name="signout"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
