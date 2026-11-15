import pandas as pd
REQUIRED=["date","product_id","category","price","unit_cost","units_sold","promotion","month","store_id"]
def load_data(path):
    df=pd.read_csv(path,parse_dates=["date"])
    missing=sorted(set(REQUIRED)-set(df.columns))
    if missing: raise ValueError(f"Missing columns: {missing}")
    if (df[["price","unit_cost","units_sold"]]<0).any().any(): raise ValueError("Negative price, cost or units")
    return df
