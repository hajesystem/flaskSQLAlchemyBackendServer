from flask import Flask, jsonify, request
from sqlalchemy.util.compat import ue
from model import init_database, db_session
from controller.userController import adminUser
from controller.infoController import adminInfo

app = Flask(__name__)
app.debug = True


@app.before_first_request
# app 실행시 처음 한번만 실행
def beforeFirstRequest():
    print('데이터베이스 연결')
    init_database()  # 데이터베이스 테이블 생성


@app.teardown_appcontext
# app의 애플리케이션 컨텍스트가 내려갈 떄마다 실행
# 요청이 들어오기 전에 만들어지고 요청이 끝날 때마다 제거된다.
# 데이터베이스 연결을 종료
def tearDownAppContext(exeption):
    print("데이터베이스 세션 종료")
    db_session.remove()


app.register_blueprint(adminUser)
app.register_blueprint(adminInfo)


@app.route('/')
def index():
    return jsonify({"message": "flask SQLAlchemy API SERVER"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4002)
