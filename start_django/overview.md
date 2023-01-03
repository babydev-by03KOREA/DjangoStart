blog > App folder
start_django > project's configuring folder

# Start
start_django > start_django > urls.py
설정 urls 파일에 / 요청이 들어오면 blog.urls를 포함하세요.

blog.urls.py 참조 > 앱.url인 /로 요청이 오면, views.py에 index 함수를 실행하세요.
>> localhost:8000/ >>> Main Screen!!!

postgreSQL > ORDBMS 사용하여 구현
pip3 install --no-binary :all: psycopg2 / PostgreSQL driver for Python
settings.py 설정파일에 APP(blog) 추가 및 DATABASES 항목을 추가.

models.py에 model은 테이블을 정의하는 클래스를 의미한다. [ORM]
blog 앱에서 DB 내부에 Post table 생성한다. 우리가 작성한 코드에는 name, content만 갖고, id는 자동생성된다.
작성 후 makemigrations > migrate 작업을 실행한다.
<a href="https://velog.io/@hxyxneee/Migration으로-똑똑하게-DB-관리하기">[migration]</a>
즉 DB에 현재 상황을 반영(이주)해보자!
모델을 생성하면 ORM이 migration 파일을 생성하고, migration 파일이 DB에 적용된다.
Models -> Migrations -> DB

Admin 계정 만들기
python3 manage.py createsuperuser
post 모델을 admin 페이지에서 보기 위해서 이를 admin 페이지에 등록 해줘야 한다!
blog(app) > admin.py에 admin.site.register(Post)로 admin 페이지에 등록해준다!