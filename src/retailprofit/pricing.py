import numpy as np, pandas as pd
from sklearn.linear_model import LinearRegression
from .features import make_features
def estimate_elasticity(df):
    d=df[(df.price>0)&(df.units_sold>0)]
    if len(d)<10: return None
    m=LinearRegression().fit(np.log(d[["price"]]),np.log(d.units_sold))
    return float(m.coef_[0])
def optimize_price(model,row,elasticity=None,max_change_pct=.15):
    current=float(row["price"]); cost=float(row["unit_cost"])
    lo=max(current*(1-max_change_pct),cost*1.001)
    hi=current*(1+max_change_pct)
    if lo>hi: return {"recommended_price":current,"expected_units":None,"expected_revenue":None,"expected_gross_profit":None,"status":"No feasible price above unit cost"}
    candidates=np.linspace(lo,hi,41); results=[]
    for price in candidates:
        sample=pd.DataFrame([{"price":price,"unit_cost":cost,"promotion":float(row.get("promotion",0)),"month":int(row.get("month",1))}])
        units=max(0.,float(model.predict(make_features(sample))[0]))
        if elasticity is not None: units*=float((price/current)**elasticity)
        results.append((price,units,price*units,(price-cost)*units))
    p,u,r,g=max(results,key=lambda z:z[3])
    return {"recommended_price":round(float(p),2),"expected_units":round(float(u),2),"expected_revenue":round(float(r),2),"expected_gross_profit":round(float(g),2),"status":"Recommendation generated"}
