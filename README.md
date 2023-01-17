 #LIMENET BACKEND

1. Anaconda python 설치

2. 가상환경 생성 및 실행

```python
conda create --name ${가상환경이름} python=3.8
conda activate ${가상환경이름}
```

3. 패키지 설치
- 사용한 패키지와 버전을 `requirements.txt`에 명시

```python
pip install -r requirements.txt
```

4. 서버구동

*로컬
```python
python manage.py runserver --settings=config.settings.local 
```

*프로덕트
```python
python3 manage.py runserver --settings=config.settings.prod 
```                 

5. Directory 구조 및 파일
    #####app
  - accounts : 계정 및 권한 app
  - {업무명칭} : 업무 서비스 app 
  - config : 프로젝트 전역 settings.py 및 url 등
    
    #####file  
  - views.py : 비지니스 로직
  - urls.py : url 경로 설정
  - models.py : DB 모델 정의

### 내부망에서 PACKAGE 설치 방법

1. 서버에서 필요 PACKAGE 설치 (Online server)

```python
# 필요 package가 requirements.txt 전체일때
pip download -d ./pip_packages/ -r requirements/dev.txt
        # down받을 폴더경로 지정

# 필요 package가 하나일때
pip download -d ./pip_packages/ pandas==1.3.6
```

2. server에서 pip_packages 폴더를 ftp를 이용해 pc로 복사 (Offline PC)

```python
pip install --no-index --find-links=./pip_packages -r ./requirements/dev.txt
# find-links : server에서 받아온 package폴더 위치
```