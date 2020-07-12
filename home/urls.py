from django.urls import path
from home import views

urlpatterns = [
    path('',views.json,name="jsondata"),
    path('home/',views.index,name="home"),
]