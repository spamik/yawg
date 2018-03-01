from django.urls import path
from yawgcore import views

urlpatterns = [
    path('', views.list_gallery),
    path('browse/<path:url>', views.list_gallery),
]
