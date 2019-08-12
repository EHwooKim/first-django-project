# Django

## 01. 시작하기

```bash
$ pip install django
```

* 현재 활용하고 있는 버전은 다음과 같다.
  * python 3.7.4
  * django 2.2.4

### 1. Django 프로젝트 시작

```bash
$ mkdir __프로젝트 이름/폴더 이름__
$ cd __프로젝트 이름/폴더 이름__
```

```bash
$ django-admin startproject __프로젝트이름__ .
```

* 프로젝트이름으로 구성된 폴더와 `manage.py`가 생성된다.
  * `__init__.py` : 해당 폴더가 패키지로 인식될 수 있게끔 작성되는 파일
  * `settings.py` : **django 설정과 관련된 파일**
  * `urls.py` : **url관리**
  * `wsgi.py` : 배포시 사용(web server gateway interface : 파이썬에서 사용되는 웹 서버)
  * `manage.py` : **django 프로젝트와 관련된 커맨드라인(명령어) 유틸리티** (명령어 실행에 도움을 준다.)

### 2. 서버 실행

```bash
$ python manage.py runserver
```

* `localhost:8000` 으로 들어가서 로켓 확인!



### 3. App 시작

```bash
$ python manege.py startapp __app이름__
```

* `app이름`인 폴더가 생성되며, 구성하고 있는 파일은 다음과 같다.

  * `admin.py` : 관리자 페이지 설정

  * `apps.py` : app의 정보 설정. 직접 수정하는 경우 별로 없음.

  * `models.py` : **MTV - Model을 정의 하는 곳**

  * `tests.oy` : 테스트 코드를 작성하는 곳

  * `views.py` : **MTV - View를 정의하는 곳.**

    * 사용자에게 요청이 왔을 때, 처리되는 함수 (중개한다고 생각하면 된다..)

      ```python
      def index(request):  # 반드시 인자로 request 넣어줘야 한다.
          return render(request, index.html)
      ```

**app을 만들고 나서 반드시 `settings.py`에서 `INSTALLED_APPS`에 app을 등록한다.**

```python
# first_django/settings.py
#..
INSTALLED_APPS = [
    'pages',
    'django.contrib.admin'
    # ...
]
# ..
```



## 02. 작성 흐름

### 1. URL 정의

```python
# first_django/urls.py
from pages import views

urlpatterns = [
    path('',views.index),   # 마지막에 , 찍는거 잊지 말자.
]
```

* `urls.py`는 우리의 웹 어플리케이션 경로들을 모두 관리한다.
* 요청이 들어오면 `urls.py`의 `urlpatterns`에 정의된 경로로 매핑한다.
* path(`경로`, `views에 정의된 함수`)

### 2. Veiw 정의

```python
# page/view.py

def index(request):
    return render(request, 'index.html')
```

* `view.py`는 MTV에서 View에 해당한다.
* 일종의 중간관리자로 Model, Template 등의 처리를 담당한다.``

### 3. Tempalte 정의

* 기본적으로 app을 생성하면, `templates` 폴더가 없으므로 직접 생성해야 한다.

```html
<!-- pages/templates/index.html -->
<h1>
    장고 안녕!
</h1>	
```

### 4. 서버 실행 및 확인

```bash
$ python manage.py runserver
```

>  `localhost:8000`에서 확인 해보자!!







