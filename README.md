(1) User
- email
- password
- nickname
- is_business

(2) Video
- title
- description
- link
- views_count
- thumbnail
- video_file: link
- User: FK

ex) 파일(이미지, 동영상)
=> 장고에 부하가 걸림.
=> S3 Bucket(저렴, 속도가 빠름) -> 결과물: 링크

(3) Reaction
- User: FK
- Video: FK
- reaction (like, dislike, cancel) => 실제 youtube rest api

(4) Comment
- User: FK
- Video: FK
- content
- like
- dislike

(5) Subscription
- User: FK => subscriber (내가 구독한 사람)
- User: FK => subscribed_to (나를 구독한 사람)

(6) Common
- created_at
- updated_at


# django-youtube-restapi

# (1) Project Settings

- GitHub

 Docker 정리

# Docker란?

> Docker는 **애플리케이션을 컨테이너라는 단위로 격리해서 실행할 수 있도록 해주는 가상화 기술**입니다.

- 개발 → 테스트 → 배포까지 환경을 통일시켜줍니다.
- 어디서 실행하든 **동일한 결과**를 보장해줍니다.
- **"작동하는 코드를 통째로 박스에 담아 옮기는 느낌!"**

---

#  Docker 구성요소

| 구성요소 | 설명 |
|----------|------|
| **Dockerfile** | 이미지 생성을 위한 설정파일 (레시피) |
| **Image** | 애플리케이션 + 환경이 포함된 실행 패키지 |
| **Container** | Image를 실제로 실행한 인스턴스 |
| **Docker Engine** | 도커를 실제로 실행시키는 시스템 |
| **Docker Hub** | 이미지 저장/공유할 수 있는 GitHub같은 곳 |

---

#  Docker Image와 Container의 차이

| 구분 | 설명 | 비유 |
|------|------|------|
| **Image** | 실행 가능한 파일(설정, 코드 등 포함) | 📀 레시피 CD |
| **Container** | 이미지가 실행 중인 상태 | 🍳 요리된 음식 |

- 하나의 이미지를 여러 개의 컨테이너로 실행 가능
- 이미지는 변하지 않지만, 컨테이너는 상태를 가짐

# 📘 CI/CD와 GitHub Actions, PostgreSQL의 장점

## 🔧 CI/CD란?

CI/CD는 **지속적 통합(Continuous Integration)** 과 **지속적 배포(Continuous Deployment)** 의 약자입니다.

- **CI (Continuous Integration)**: 개발자가 코드를 자주 병합(Merge)하고 테스트하는 방식
- **CD (Continuous Deployment)**: 테스트를 통과한 코드를 자동으로 서버에 배포하는 방식

### ✅ CI/CD의 장점
- 수동 배포 과정을 자동화하여 **시간 절약**
- 테스트 자동화로 **버그 조기 발견**
- 코드 품질 향상 및 팀 생산성 증가

---

## ⚙️ GitHub Actions란?

> GitHub에서 제공하는 **자동화 도구**로, CI/CD를 쉽게 구현할 수 있는 기능입니다.

### ✨ 특징
- `.github/workflows/*.yml` 파일로 설정
- 코드 푸시나 PR 시 자동으로 테스트, 빌드, 배포 가능
- 다양한 오픈소스 액션(Action)을 자유롭게 연결 가능

### 📄 예시 (flake8 테스트 자동화)

```yaml
name: Lint with flake8

on: [push]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install flake8
      - name: Run flake8
        run: flake8 .
