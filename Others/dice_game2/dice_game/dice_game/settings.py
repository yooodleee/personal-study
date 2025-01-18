from pathlib import Path
from decouple import config

# BASE_DIR: 프로젝트의 기본 디렉토리 경로
BASE_DIR=Path(__file__).resolve().parent.parent

# SECRET_KEY: Django 프로젝트의 보안 키
SECRET_KEY=config('SECRET_KEY') #  시스템 환경 변수 지정

# Optional: Handle missing SECRET_KEY
if not SECRET_KEY:
    raise ValueError("The SECRET_KEY environment variable is not set!")

# DEBUG: 디버그 모드 설정 (배포 시 반드시 False 설정)
DEBUG=True

# ALLOWED_HOSTS: 허용된 호스트 (배포 시 도메인 추가)
ALLOWED_HOSTS=[]

# INSTALLED_APPS: 프로젝트에서 사용하는 앱들
INSTALLED_APPS=[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'game', # 게임 앱 추가
]

# MIDDLEWARE: 미들웨어 설정
MIDDLEWARE=[
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF: URL 라우팅 설정 파일
ROOT_URLCONF='dice_game.urls'

# TEMPLATES: 템플릿 엔진 설정
TEMPLATES=[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # 템플릿 디렉토리 경로
        'APP_DIRS': True,
        'OPTIONS': {
            'context_progressors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION: WSGI 애플리케이션 경로
WSGI_APPLICATION='dice_game.wsgi.application'

# DATABASES: 데이터베이스 설정
DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# AUTH_PASSWORD_VALIDATIORS: 비밀번호 검증 규칙
AUTH_PASSWORD_VALIDATIORS=[
     {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# LANGUAGE_CODE: 기본 언어
LAGUAGE_CODE='en-us'

# TIME_ZONE: 기본 시간대
TIME_ZONE='UTC'

# USE_I18N: 국제화 지원 여부
USE_I18N=False

# USE_TZ: 시간대 지원 여부
USE_TZ=True

# STATIC_URL: 정적 파일 URL 경로
STATIC_URL='static/'

# DEFAULT_AUTO_FILED: 기본 자동 필드 유형
DEFALUT_AUTO_FIELD='django.db.models.BigAutoField'