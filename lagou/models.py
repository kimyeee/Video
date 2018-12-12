from sqlalchemy import Column, String, create_engine, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class Lagou(Base):
    # 表的名字:
    __tablename__ = 'lagou'

    id = Column(Integer(), primary_key=True)
    company = Column(String(64))
    name = Column(String(64))
    salary = Column(String(64))
    city = Column(String(32))
    experience = Column(String(32))
    education = Column(String(32))
    job_type = Column(String(32))
    release_time = Column(String(64))
    labels = Column(String(64))
    advantage = Column(String(128))
    description = Column(String(1024))
    address = Column(String(128))
    publisher = Column(String(32))
    hr_position = Column(String(32))
    aspiration = Column(String(32))
    domain = Column(String(32))
    phase = Column(String(32))
    investment = Column(String(255))
    scale = Column(String(64))
    home_page = Column(String(64))
    company_labels = Column(String(64))


# engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/test", max_overflow=5)
# Session = sessionmaker(bind=engine)
# session = Session()
# obj = Lagou(name='a')
# session.add(obj)
# session.commit()
# session.close()

