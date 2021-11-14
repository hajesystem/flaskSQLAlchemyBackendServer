from sqlalchemy import Column, String, Integer, Date, Boolean
from marshmallow import Schema, post_load, fields
from model import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userName = Column(String(32), unique=True)
    password = Column(String(255))
    email = Column(String(80))
    startDay = Column(Date)
    accounting = Column(Boolean)

    def __init__(self, userName, password, email, startDay, accounting):
        self.userName = userName
        self.password = password
        self.email = email
        self.startDay = startDay
        self.accounting = accounting


class UserSchema(Schema):
    class Meta:
        fields = ("id", "userName", "password",
                  "email", "startDay", "accounting")

    @post_load
    def make_user(self, data, **kwargs):
        return Users(**data)


userSchema = UserSchema()
