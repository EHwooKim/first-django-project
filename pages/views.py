import random

from django.shortcuts import render


# Create your views here.

# 2. 요청을 처리할 함수 정의
def index(request):
    # 2. >> 로직 작성 <<
    # 3. 해당하는 템플릿 반환
    return render(request, 'index.html')   


def hello(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)

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
    return render(request, 'lotto.html', context)
