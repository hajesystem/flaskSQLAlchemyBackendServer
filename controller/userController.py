from flask import Blueprint, jsonify, request
from sqlalchemy import insert, select
from sqlalchemy.exc import SQLAlchemyError
from model import db_session
from model.userModel import Users, userSchema

adminUser = Blueprint('user', __name__, url_prefix='/admin')


@adminUser.route('user', methods=['GET'])
def getAll():
    # sql = db_session.query(Users).filter(Users.userName == "kimhanjun").first()
    # result = userSchema.dump(users, many=True)
    sql = select(Users).where(Users.userName == "kimhanjun")
    aaa = db_session.scalar(sql)
    result = userSchema.dump(aaa)
    return jsonify(result)


@adminUser.route('user', methods=['POST'])
def add():
    try:
        userName = request.json['userName']
        password = request.json['password']
        email = request.json['email']
        startDay = request.json['startDay']
        accounting = bool(request.json['accounting'])
        sql = insert(Users).values(userName=userName, password=password,
                                   email=email, startDay=startDay, accounting=accounting)
        db_session.execute(sql)
        # user = Users(userName, password, email)
        # db_session.add(user)
        db_session.commit()
        return jsonify({"state": "success"})
    except SQLAlchemyError as error:
        db_session.rollback()
        print("Error >>", error)
        return jsonify({"error": str(error)})
    finally:
        pass


@adminUser.route('load', methods=['POST'])
def addLoad():
    try:
        load = request.json['load']
        userData = userSchema.load(load)
        print(userData.userName, userData.password)
        # sql = insert(Users).values(userName=userData.us)
        # db_session.execute(sql)
        # user = Users(userName, password, email)
        # db_session.add(user)
    #     db_session.commit()
        return jsonify({"state": "success"})
    # except SQLAlchemyError as error:
    #     db_session.rollback()
    #     print("Error >>", error)
    #     return jsonify({"error": str(error)})
    finally:
        pass


@adminUser.route('user/<id>', methods=['PUT'])
def update(id):
    try:
        userName = request.json['userName']
        password = request.json['password']
        email = request.json['email']

        user = db_session.query(Users).get(id)
        user.userName = userName
        user.password = password
        user.email = email
        db_session.commit()
        return userSchema.dump(user)
    except SQLAlchemyError as error:
        db_session.rollback()
        print("Error >>", error)
        return jsonify({"error": str(error)})
    finally:
        pass


@adminUser.route('user/<id>', methods=['DELETE'])
def delete(id):
    try:
        user = db_session.query(Users).get(id)
        db_session.delete(user)
        db_session.commit()
        return userSchema.dump(user)
    except SQLAlchemyError as error:
        db_session.rollback()
        print("Error >>", error)
        return jsonify({"error": str(error)})
    finally:
        pass
