from sqlalchemy import Column, Integer, String,Float,Date
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.sql.sqltypes import Float
Base = declarative_base()


class userModel(Base):
    __tablename__='users'
    idf=Column(Integer, autoincrement=True , primary_key=True)
    user_id = Column(String)

class productModel(Base):
    __tablename__='products'
    idf=Column(Integer, autoincrement=True , primary_key=True)
    user_id = Column(String)
    product_id= Column(String)
    date= Column(Date)
    amount= Column(Float)
    status= Column(String)

class investor(Base):
    __tablename__ = 'investor'
    idf = Column(Integer, autoincrement=True , primary_key=True)
    name = Column(String)
    
class investorInfoModel(Base):
    __tablename__='investors'
    idf=Column(Integer, autoincrement=True , primary_key=True)
    product_id= Column(String)
    investor_name= Column(String)
    sold= Column(Float)
    purchased= Column(Integer)
    left_amount= Column(Float)
    remaining= Column(Integer)

