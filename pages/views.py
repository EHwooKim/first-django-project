import random
import datetime
from django.shortcuts import render


# Create your views here.

# 2. 요청을 처리할 함수 정의
def index(request):
    # 2. >> 로직 작성 <<
    # 3. 해당하는 템플릿 반환
    return render(request, 'pages/index.html')   


def hello(request, name):
    context = {'name': name}
    return render(request, 'pages/hello.html', context)

# 값 넘겨주는 방법.
def lotto(request):
    print(request)
    print(type(request))
    print(request.META)
    # (파이썬) 로직이 들어가고
    jackpot = sorted(random.sample(range(1, 46), 6))
    rank = random.choice(range(1, 6))
    # 값을 딕셔너리에 담아서 (보통 context라고 부름) 보낸다.
    context = {'jackpot': jackpot, 'rank': rank}  
    # render할 때 3번째 인자로 넘겨준다.
    # redner 함수의 필수!! 인자 : request, template 파일 !
    # 변수를 넘겨주고 싶으면 3번째 인자로 dictionary를 넘겨준다.
    # Django에서 활용하는 템플릿 언어는 Django Template Language (DTL)!  ( 출력할 떄 중괄호 두개 쓰는 그거 ) 
    return render(request, 'pages/lotto.html', context)

def dinner(request):
    menus = ['롯데리아', '편의점', '맘스터치', '응급실떡볶이', '노은각', '피자', '치킨']
    pick = random.choice(menus)
    context = {
        'pick': pick, 
        'menus': menus, 
        'users': [], 
        'sentence': 'Life is short, You need Python + django!', 
        'datetime_now': datetime.datetime.now(),
        'google_link': 'https://www.google.com'
        }
    return render(request, 'pages/dinner.html', context)


def cube(request, num):
    context = {'num':num, 'cube_num':num**3, 'numbers':[1, 2, 3, 4, 5]}
    return render(request, 'pages/cube.html', context)


def about(request, name, age):
    context = {'name': name, 'age': age}
    return render(request, 'pages/about.html', context)

def isitgwangbok(request):
    today = datetime.datetime.now()
    if today.month == 8 and today.day == 15:
        answer = '예'
    else: answer = '아니요'
    context = {
        'today': today,
        'answer': answer
    }
    return render(request,'isitgwangbok.html', context)

def ping(request):
    return render(request,'ping.html')

def pong(request):
    # 사용자가 넘겨주는 값 받아오기 (META가 어디에 담겨서 온다그랬지? request!! GET도 마찬가지.)
    print(request.GET) # 찍어보니 딕셔너리 안에 리스트로 값이 넘어오지? QuertDict
    # QueryDict {'data':'안녕하세요'}
    data = request.GET.get('data')
    context = {
        'data': data
    }
    return render(request, 'pages/pong.html', context)

def signup(request):
    return render(request,'signup.html')


def signup_result(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password_confirmation = request.POST.get('password_confirmation')

    if password == password_confirmation:
        result = True
    else:
        result = False

    context = {
        'username': username,
        'result': result
    }
    return render(request, 'pages/signup_result.html', context)

def movie(request):
    return render(request, 'pages/movie.html')