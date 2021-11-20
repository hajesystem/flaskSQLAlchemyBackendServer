from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from model import db_session
from model.infoModel import Info, infoSchema

adminInfo = Blueprint('info', __name__, url_prefix='/admin')


@adminInfo.route('info', methods=['GET'])
def getAll():
    info = db_session.query(Info).all()
    result = infoSchema.dump(info, many=True)
    return jsonify(result)


@adminInfo.route('info', methods=['POST'])
def add():
    try:
        sex = request.json['sex']
        address = request.json['address']
        phone = request.json['phone']
        info = Info(sex, address, phone)
        db_session.add(info)
        db_session.commit()
        return infoSchema.dump(info)
    except SQLAlchemyError as error:
        db_session.rollback()
        print("Error >>", error)
        return jsonify({"error": str(error)})
    finally:
        pass


@adminInfo.route('info/<id>', methods=['PUT'])
def update(id):
    try:
        sex = request.json['sex']
        address = request.json['address']
        phone = request.json['phone']

        info = db_session.query(Info).get(id)
        info.sex = sex
        info.address = address
        info.phone = phone
        db_session.commit()
        return infoSchema.dump(info)
    except SQLAlchemyError as error:
        db_session.rollback()
        print("Error >>", error)
        return jsonify({"error": str(error)})
    finally:
        pass


@adminInfo.route('info/<id>', methods=['DELETE'])
def delete(id):
    try:
        info = db_session.query(Info).get(id)
        db_session.delete(info)
        db_session.commit()
        return infoSchema.dump(info)
    except SQLAlchemyError as error:
        db_session.rollback()
        print("Error >>", error)
        return jsonify({"error": str(error)})
    finally:
        pass
