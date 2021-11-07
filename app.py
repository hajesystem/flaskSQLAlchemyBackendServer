from flask import Flask, jsonify, request
from sqlalchemy.util.compat import ue
from model import init_database, db_session
from model.userModel import Users, userSchema

app = Flask(__name__)
app.debug = True


@app.before_first_request
# app 실행시 처음 한번만 실행
def beforeFirstRequest():
    print('데이터베이스 연결')
    init_database()


@app.teardown_appcontext
# app의 애플리케이션 컨텍스트가 내려갈 떄마다 실행
# 요청이 들어오기 전에 만들어지고 요청이 끝날 때마다 제거된다.
# 데이터베이스 연결을 종료
def tearDownAppContext(exeption):
    print("데이터베이스 세션 종료")
    db_session.remove()


@app.route('/')
def index():
    return jsonify({"message": "flask SQLAlchemy API SERVER"})


@app.route('/users', methods=['POST'])
def addUsers():
    print(request.json)
    userName = request.json['userName']
    password = request.json['password']
    email = request.json['email']

    user = Users(userName, password, email)
    db_session.add(user)
    db_session.commit()
    return userSchema.dump(user)


@app.route('/users', methods=['GET'])
def getUsers():
    users = db_session.query(Users).all()
    result = userSchema.dump(users, many=True)
    return jsonify(result)


@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    user = db_session.query(Users).get(id)
    userName = request.json['userName']
    password = request.json['password']
    email = request.json['email']

    user.userName = userName
    user.password = password
    user.email = email
    db_session.commit()
    return userSchema.dump(user)


@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    user = db_session.query(Users).get(id)
    db_session.delete(user)
    db_session.commit()
    return userSchema.dump(user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4002)
