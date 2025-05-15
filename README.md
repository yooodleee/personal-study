# 프로젝트 이름

> Flutter 기반의 면접 진행 앱 - DevOps 및 백엔드 인프라 구현 중심

## 📌 프로젝트 개요

Flutter와 Vue3/Nuxt3를 기반으로 한 면접 앱으로, 면접자와 면접관 간의 인터뷰를 실시간으로 진행할 수 있습니다. 본 프로젝트에서는 **DevOps 엔지니어**로서 다음과 같은 인프라, CI/CD, 배포, 모니터링, 협업 환경을 구축 및 운영하였습니다.

## 🧰 사용 기술 스택

### 🖥️ Frontend
- `Flutter`, `Dart`: 모바일 앱 개발
- `Vue3`, `Nuxt3`, `Vuetify3`: 웹 기반 관리자 도구 및 대시보드 구현
- `Typescript`, `HTML5/CSS3`, `Javascript`

### 🛠️ Backend & API
- `Python`, `Django`, `FastAPI`: 사용자 인증, 면접 로직, OpenAI API 연동
- `MySQL`, `FAISS`: 데이터 저장 및 벡터 검색 기반 유사 질문 제공

### ☁️ DevOps / Infrastructure
- `AWS EC2`, `S3`, `CloudFront`, `Route53`: 백엔드 서버, 정적 자산 배포, DNS 관리
- `Github Actions`: CI/CD 자동화 (Flutter 빌드, 백엔드 배포 파이프라인 구축)
- `OAuth`, `Domain Driven Design`, `Agile Methodologies`

### 🔧 Tools & Collaboration
- `Github`, `Slack`, `Notion`, `Discord`: 이슈 관리, 릴리즈 협업, 커뮤니케이션

---

## 🚀 주요 DevOps 구현 사항

### 1. CI/CD 파이프라인 자동화
- `Github Actions`를 활용해 **Flutter 앱 빌드 → Google Play 배포 자동화**
- Django/FastAPI 백엔드의 **Lint/Test → Docker Build → EC2 배포 자동화**

### 2. 인프라 구성 (AWS)
- `EC2`: 웹/백엔드 서버 호스팅
- `S3 + CloudFront`: 정적 리소스 및 Flutter 웹 배포
- `Route53`: 도메인 관리 및 HTTPS 적용
- `IAM 정책`: 보안 최소 권한 설정

### 3. AI 기능 연동 (OpenAI)
- OpenAI API를 활용하여 면접 질문 자동 생성 및 평가 기능 구현
- FAISS 기반 유사 질문 검색 기능 연동

### 4. 협업 및 문서화
- Notion을 통한 기술 문서 및 API 명세 관리
- Slack/Discord으로 CI 상태 알림 및 코드 리뷰 소통

---

## 📱 기능 예시

- 앱 내에서 실시간 면접 기능
- 질문 추천 및 면접 평가
- 관리자 페이지 (Nuxt3 기반)에서 면접 관리
- 질문 데이터 기반 검색 및 추천 기능 (FAISS)

---

## 🧑‍💻 DevOps 직무에서의 기여

- 전체 배포 파이프라인 설계 및 구축
- CI/CD 자동화 및 빌드 상태 모니터링 설정
- AWS 기반 인프라 구축 및 보안 구성
- 협업 환경 및 코드 관리 체계 정립

---

## 📦 배포 및 운영

| 항목 | 내용 |
|------|------|
| 앱 배포 | Google Playstore 등록 |
| 백엔드 서버 | AWS EC2 + Nginx + Gunicorn |
| 정적 파일 | AWS S3 + CloudFront |
| 도메인 | AWS Route53 |
| 인증 방식 | OAuth2 기반 로그인 |
| AI API | OpenAI GPT 연동 |

---

## 📎 관련 링크
- 📲 [Google Playstore 앱 링크](#)
- 🗂 [기술 문서 Notion 페이지](#)
- 📈 [CI/CD 상태 대시보드 (Github Actions)](#)

