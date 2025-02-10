# 1단계: 빌드 단계
FROM node:18-alpine AS builder

# 작업 디렉토리 설정
WORKDIR /app

# package.json과 package-lock.json 복사
COPY package*.json ./

# 필요한 패키지 설치
RUN npm install --legacy-peer-deps

# 소스 코드 복사
COPY . .

# Nuxt의 production 모드로 빌드
RUN npm run build

# 2단계: 실행 단계
FROM node:18-alpine

# 작업 디렉토리 설정
WORKDIR /app

# 빌드된 결과만 복사
COPY --from=builder /app ./

# 포트 설정 (Nuxt 기본 포트는 3000)
EXPOSE 3000

# 컨테이너가 실행될 때 실행할 명령어 (production 모드)
CMD ["npm", "run", "start"]
