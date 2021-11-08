# flask SQLAlchemy Backend Server
1. 사용 패키지
* pip install flask
* pip install SQLAlchemy
* pip install marshmallow
* pip install pymysql

2. 구조
#
├── app.py #
├── .gitignore #
├── config.py #
├── controller : 모델과 관련된 모든 송수신, HTTP 요청을 처리  <flask blueprint사용> #
│     └── userController.py #
│     └── infoController.py #
└── model : 데이터 베이스 모델 정의 #
      └── userModel.py #
      └── infoModel.py #
