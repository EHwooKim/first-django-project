"""first_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # 1. url 설정
    # path(url, 해당하는 views의 함수)
    path('', views.index),
    # /hello 로 들어오면 인사하기
    # variable routing
    # url에 특정 값을 변수처럼 활용!
    path('hello/<str:name>/', views.hello),
    # /lotto 로 들어오면 번호 추첨하기
    path('lotto/', views.lotto),
    path('dinner/', views.dinner),
    path('cube/<int:num>/',views.cube),
    path('about/<str:name>/<int:age>/', views.about),
    path('isitgwangbok/',views.isitgwangbok),
    path('ping/', views.ping),
    path('pong/', views.pong),
    # 가짜 회원가입. username, password, password_confirmation 받아서 패스워드 일치하면 '00님 회원가입 ok' 아니면 '비번 잘못'
    path('signup/', views.signup),
    path('signup_result/', views.signup_result),
    path('movie/',views.movie),
]

