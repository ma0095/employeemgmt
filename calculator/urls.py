from django.urls import path
from calculator import views

urlpatterns=[
    path("home", views.HomeView.as_view(),name="calc-home"),
    path("add",views.AddView.as_view(),name="calc-add"),
    path("sub",views.SubView.as_view(),name="calc-sub"),
    path("multiplication", views.MultiplicationView.as_view(),name="calc-multi"),
    path("division",views.DivitionView.as_view(),name="calc-div"),
    path("wordcount",views.WordcountView.as_view(),name="calc-wordcount"),
    path("prime",views.PrimeView.as_view(),name="calc-prime"),



]