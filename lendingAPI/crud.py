from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import except_
import models
import schemas

def create_product(db: Session, product_data: schemas.productSchema):
    product = models.productModel(user_id =product_data.user_id,product_id= product_data.product_id,
                                  date= product_data.date,amount=product_data.amount,
                                  status= product_data.status)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_products(db : Session, user : schemas.userSchema):
    return db.query(models.productModel).filter(models.productModel.user_id == user.user_id).all()

"""
    investors crud
"""
def get_investors(db : Session, query : schemas.investorQuery):
    return db.query(models.investorInfoModel).filter(models.investorInfoModel.product_id == query.product_id).all()

def create_investor(db : Session, investor_info : schemas.investorQuery, product_id : str):
    investor = models.investorInfoModel(product_id=product_id,investor_name=investor_info.investor_name,
                                  sold= investor_info.sold,purchased=investor_info.purchased,
                                  left_amount= investor_info.left_amount,remaining= investor_info.remaining)
    db.add(investor)
    db.commit()
    db.refresh(investor)
    return investor

def update_investor(db : Session,investor_id: str, investor_info : schemas.investorQuery):
    investor = db.query(models.investorInfoModel).filter(models.investorInfoModel.idf ==investor_id).first()
    investor.investor_name=investor_info.investor_name
    investor.sold= investor_info.sold
    db.commit()
    db.refresh(investor)
    return investor


   
def delete_investor(db: Session, investor_id: str):
    todo = db.query(models.investorInfoModel).filter(models.investorInfoModel.idf == investor_id).first()
    try:
        db.delete(todo)
        db.commit()
    except:
        return False
    return True

"""Investor"""
def create_investor_name(db : Session,investor : schemas.investorSchema):
    investor = models.investor(name=investor.name)
    db.add(investor)
    db.commit()
    db.refresh(investor)
    return investor

def get_investor_name(db: Session):
    return db.query(models.investor).all()