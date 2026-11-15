from pathlib import Path
import json,joblib,pandas as pd
from sklearn.model_selection import train_test_split
from .data import load_data
from .features import make_features
from .models import train_demand_model,metrics
from .pricing import estimate_elasticity,optimize_price
def run_pipeline(data_path="data/sample/retail_sales.csv"):
    df=load_data(data_path); X=make_features(df); y=df.units_sold.astype(float)
    a,b,c,d=train_test_split(X,y,test_size=.2,random_state=42)
    model=train_demand_model(a,c); scores=metrics(d,model.predict(b)); elasticity=estimate_elasticity(df)
    latest=df.sort_values("date").groupby("product_id").tail(1)
    rows=[]
    for _,row in latest.iterrows():
        rows.append({"product_id":row.product_id,"category":row.category,"current_price":row.price,"unit_cost":row.unit_cost,"estimated_elasticity":elasticity,**optimize_price(model,row,elasticity)})
    result=pd.DataFrame(rows)
    Path("artifacts").mkdir(exist_ok=True); Path("data/processed").mkdir(parents=True,exist_ok=True)
    joblib.dump(model,"artifacts/demand_model.joblib")
    Path("artifacts/metrics.json").write_text(json.dumps({"demand_model":scores,"pooled_elasticity":elasticity},indent=2))
    result.to_csv("data/processed/pricing_recommendations.csv",index=False)
    return scores,elasticity,result
