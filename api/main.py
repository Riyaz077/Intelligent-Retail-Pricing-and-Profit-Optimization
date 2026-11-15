from pathlib import Path
import joblib
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from src.retailprofit.pricing import optimize_price
app=FastAPI(title="RetailProfit AI API",version="1.0.0")
class Product(BaseModel):
    price:float=Field(gt=0)
    unit_cost:float=Field(ge=0)
    promotion:int=Field(ge=0,le=1)
    month:int=Field(ge=1,le=12)
@app.get("/")
def root(): return {"service":"RetailProfit AI","docs":"/docs"}
@app.post("/optimize-price")
def optimize(x:Product):
    p=Path("artifacts/demand_model.joblib")
    if not p.exists(): raise HTTPException(status_code=503,detail="Train model first using python scripts/run_pipeline.py")
    return optimize_price(joblib.load(p),x.model_dump())
