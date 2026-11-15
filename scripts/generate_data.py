from pathlib import Path
import numpy as np,pandas as pd
def generate_sales(days=240,products=18,seed=42):
    rng=np.random.default_rng(seed); dates=pd.date_range("2025-01-01",periods=days)
    cats=["Grocery","Electronics","Home","Fashion","Personal Care"]; rows=[]
    for j in range(products):
        sku=f"SKU-{j+1:03d}"; cat=cats[j%len(cats)]
        base=float(rng.uniform(8,180)); cost=base*float(rng.uniform(.42,.78))
        demand=float(rng.uniform(12,90)); elast=float(rng.uniform(-2,-.35)); store=f"STORE-{j%4+1:02d}"
        for date in dates:
            promo=int(rng.random()<.16); seasonal=1+.18*np.sin(2*np.pi*date.month/12)
            price=base*(.94 if promo else 1)*float(rng.normal(1,.025))
            mu=demand*seasonal*(price/base)**elast*(1.22 if promo else 1)
            units=int(rng.poisson(max(mu,1)))
            rows.append((date,sku,cat,round(price,2),round(cost,2),units,promo,date.month,store))
    return pd.DataFrame(rows,columns=["date","product_id","category","price","unit_cost","units_sold","promotion","month","store_id"])
if __name__=="__main__":
    Path("data/sample").mkdir(parents=True,exist_ok=True)
    generate_sales().to_csv("data/sample/retail_sales.csv",index=False)
    print("Generated synthetic retail sales data.")
