from sqlalchemy import Column, String, Integer
from marshmallow import Schema
from sqlalchemy.util.compat import u
from model import Base


class Info(Base):
    __tablename__ = "info"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sex = Column(String(10))
    address = Column(String(255))
    phone = Column(String(11), unique=True)

    def __init__(self, sex, address, phone):
        self.sex = sex
        self.address = address
        self.phone = phone


class InfoSchema(Schema):
    class Meta:
        fields = ('id', 'sex', 'address', 'phone')


infoSchema = InfoSchema()
