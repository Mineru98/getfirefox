## 설치

```sh
python --version
# Python 3.7.4
```

`pip install -r requirements.txt`

경우에 따라서 하드웨어가 gpu가 없는 경우엔 추가로 설치

`pip install tensorflow-cpu`

## 가상환경 구축

```sh
pip3 -V
# /usr/local/lib/python3.7/site-packages/pip
```

```sh
# 설치
pip install virtualenv
# 가상환경 지정
python -m virtualenv venv-tf-step-1
cd venv-tf-step-1
source bin/activate
mkdir src
cd src

# 가상환경 종료
cd ..
deactivate
```