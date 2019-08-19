from django.urls import path
# 현재 app(directory)의 views.py 를 가져옴
from . import views

urlpatterns = [
    path('', views.index),
    path('artii/', views.artii),
    path('artii_result/', views.artii_result),
    path('push/',views.push),
    path('pull/',views.pull),
]