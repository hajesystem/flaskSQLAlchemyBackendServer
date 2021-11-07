from sqlalchemy import Column, String, Integer
from marshmallow import Schema, fields
from model import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userName = Column(String(32), unique=True)
    password = Column(String(255))
    email = Column(String(80))

    def __init__(self, userName, password, email):
        self.userName = userName
        self.password = password
        self.email = email


class UserSchema(Schema):
    # id = fields.Str()
    # userName = fields.Str()
    # password = fields.Str()
    # email = fields.Str()
    class Meta:
        fields = ('id', 'userName', 'password', 'email')


userSchema = UserSchema()
