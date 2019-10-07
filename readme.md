## How to start
###### by Daewoon Kim
### 0. branch
##### branch 변경
~~~
git clone https://github.com/dwnusa/memoapp.git
git checkout -t remotes/origin/both-dwkim1
~~~
### 1. backend
##### 경로이동
~~~
cd MemoApp/backend
~~~
##### 설치 및 서버실행
~~~
python --version
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
~~~
~~~
python manage.py migrate
python manage.py runserver
~~~

#### docker

docker build & run
```sh
>> sudo docker build -t <image-name> .
>> sudo docker run -p <host-port>:<container-port> <image-name>
```

### 2. frontend
##### 경로이동
~~~
cd MemoApp/frontend
~~~
##### 설치 및 서버실행
~~~
yarn install
yarn add axios
yarn start
~~~
