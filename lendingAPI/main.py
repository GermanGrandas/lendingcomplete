import uvicorn
from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from typing import List
import schemas,crud,models
from tags import tags
# Database configuration
# SQLALCHEMY_DATABASE_URL = os.environ['SQLALCHEMY_DATABASE_URL']
SQLALCHEMY_DATABASE_URL = "sqlite:///lending.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})
engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# engine.execute("""DROP TABLE products;""")
#Create tables
# models.Base.metadata.create_all(bind=engine)
# print(engine.table_names())

def get_db():
   """provide db session to path operation functions"""
   try:
   	db = SessionLocal()
   	yield db
   finally:
   	db.close()

app = FastAPI(openapi_tags=tags, title="LendingTest API",docs_url=None, #"/api/docs",
              description = "API created to offer functionality to the LendingFront technical test")

app.mount("/static", StaticFiles(directory="static"), name="static")
origins = [
    "http://localhost",
    "localhost",
    "http://localhost:3000",
    "localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
"""Docs"""
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )

@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()

"""Products"""
@app.post('/api/create_product',tags=["create_product"])
async def create_product(product : schemas.productSchema,db: Session = Depends(get_db)):
    product_info = crud.create_product(db,product)
    if product_info:
        return JSONResponse(status_code=200, content={"message": f"the product was correctly saved"})
    else:
        return JSONResponse(status_code=500, content={"message": f"Something Happened"})
        
@app.post('/api/products_by_id',response_model=List[schemas.productSchema], description="Bring all products given a user id")
def get_products(user :schemas.userSchema,db: Session = Depends(get_db)):
    results = crud.get_products(db,user)
    return results

"""
    Investor Queries
"""
@app.post("/api/get_investor_by_id",response_model=List[schemas.investorInfoSchema],
          description = "Bring all the investors of a given product")
def get_investors(query :schemas.investorQuery, db: Session = Depends(get_db)):
    results = crud.get_investors(db,query)
    return results

@app.post("/api/create_investor/{product_id}",description = "Create a new investor for a given product_id ")
def get_investors(investor_info :schemas.investorInfoSchema,product_id : str, db: Session = Depends(get_db)):
    result = crud.create_investor(db,investor_info,product_id)
    if result:
        return JSONResponse(status_code=200, content={"message": f"the investor was correctly saved"})
    else:
        return JSONResponse(status_code=500, content={"message": f"Something Happened"})
    
@app.put("/api/edit_investor/{investor_id}",description="Edit the information from a investor")
def edit_investor(investor_id: str,investor_info :schemas.investorUpdate,db: Session = Depends(get_db)):
    result = crud.update_investor(db,investor_id,investor_info)
    if result:
        return JSONResponse(status_code=200, content={"message": f"the investor was correctly edited"})
    else:
        return JSONResponse(status_code=500, content={"message": f"Something Happened"})
    
@app.delete("/api/delete_investor/{investor_id}",description="Delete an investor from a given product")
def delete_investor(investor_id: str,db: Session = Depends(get_db)):
    result = crud.delete_investor(db,investor_id)
    if result:
        return JSONResponse(status_code=200, content={"message": f"the investor was correctly deleted"})
    else:
        return JSONResponse(status_code=500, content={"message": f"Something Happened"})
    
"""Investor Name"""
@app.get("/api/get_investor_names", description="Get all the investors available in the platform")
def get_investor_name(db: Session = Depends(get_db)):
    result = crud.get_investor_name(db)
    return result

@app.post("/api/create_investor_name", description="Create a new investor for the platform")
def create_investor_name(investor_info :schemas.investorSchema,db: Session = Depends(get_db)):
    result = crud.create_investor_name(db,investor_info)
    if result:
        return JSONResponse(status_code=200, content={"message": f"the investor was correctly deleted"})
    else:
        return JSONResponse(status_code=500, content={"message": f"Something Happened"})
    
@app.get("/")
def home():
    return {"Hello": "FastAPI"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)