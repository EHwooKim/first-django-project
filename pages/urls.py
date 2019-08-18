from django.urls import path
from . import views  # 같은 디렉토리에서 views를 가져오겠다! 그래서 . 찍은거야

urlpatterns = [
    path('', views.index),
    path('hello/<str:name>/', views.hello),
    path('lotto/', views.lotto),
    path('dinner/', views.dinner),
    path('cube/<int:num>/',views.cube),
    path('about/<str:name>/<int:age>/', views.about),
    path('isitgwangbok/',views.isitgwangbok),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('signup/', views.signup),
    path('signup_result/', views.signup_result),
    path('nav/',views.nav),
    path('movie/',views.movie),
]
