"""
Model = 데이터베이스 정의

모델이란 사용될 데이터에 대한 정의를 담고 있는 장고의 클래스이다.
장고는 ORM 기법을 사용하여 애플리케이션에서 사용할 데이터베이스를 클래스로 매핑해서 코딩할 수 있다.
즉, 하나의 모델 클래스는 하나의 테이블에 매핑되고, 모델 클래스의 속성은 테이블의 칼럼에 매핑된다.

이렇게 ORM 기법을 사용해 테이블을 클래스로 매핑하면, 애플리케이션에서는 데이터베이스에 대한 액세스를 SQL 없이도
클래스를 다루는 것처럼 할 수 있어 편리하다. 또한 SQLite3, MYSQL, PostgreSQL 등 데이터베이스 엔진을 변경하더라도 ORM을 통한 
API는 변경할 필요가 없기 때문에, 필요에 따라 데이터베이스 엔진을 훨씬 쉽게 변경할 수 있다.

장고의 ORM 기법에 대한 이해를 돕기 위해 Person이라는 테이블, 즉 장고의 Person 모델 클래스를 정의해보겠다.
이러한 모델 클래스는 models.py 파일에 정의한다.
"""
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

# Person 모델은 장고 내부적으로 SQL 명령을 사용하여 다음과 같은 데이터베이스 테이블을 생성한다.

# CREATE TABLE myapp_person (
#     "id" serial NOT NULL PRIMARY KEY,
#     "first_name" varchar(30) NOT NULL,
#     "last_name" varchar(30) NOT NULL
# );

'''
장고는 모델 클래스로부터 테이블을 자동으로 생성하기 위해 models.py 파일에 정의된 모델 클래스를 해석하고
여러 가지 규칙을 적용한다. 이러한 테이블 자동 생성에 관한 자세한 설명은 다음 페이지를 참고하길 바란다.
https://docs.djangoproject.com/en/2.1/topics/db/models

장고는 테이블을 모델 클래스로 정의하고 이를 실제 데이터베이스에 반영한 후에도 테이블에 데이터를 입력하고 
입력된 데이터를 확인 및 변경할 수 있는 여러 가지 기능을 제공하고 있다.
'''