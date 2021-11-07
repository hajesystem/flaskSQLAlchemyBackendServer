from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# DB설정 가져오기(가상환경에서 sys안됨)
# import sys
# sys.path.append('/home/hanjun/study/pythonSqlAlchemyFlask')
import config

# 연결설정 create_engine()
engine = create_engine(config.mysql_conn, echo=True,
                       convert_unicode=True, future=True)

# Session 생성
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

# 매칭선언 declarative_base() : 테이블에 Mapping될 클래스를 정의하는 작업에 필요. Mapping에 필요한 클래스를 생성
Base = declarative_base()
# query_property() : select 할 속성을 Base에 미리 담아둔다
Base.query = db_session.query_property()


def init_database():
    # Base 생성
    Base.metadata.create_all(bind=engine)
