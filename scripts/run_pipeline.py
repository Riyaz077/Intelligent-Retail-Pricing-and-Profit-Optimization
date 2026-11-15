from pathlib import Path
from scripts.generate_data import generate_sales
from src.retailprofit.pipeline import run_pipeline
if __name__=="__main__":
    p=Path("data/sample/retail_sales.csv")
    if not p.exists(): generate_sales().to_csv(p,index=False)
    m,e,r=run_pipeline(str(p)); print("Metrics:",m,"Elasticity:",e); print(r.head())
