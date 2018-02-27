from django.urls import path
from yawgcore import views

urlpatterns = [
    path('', views.hello_world),
    path('test/', views.hello_world),
]
