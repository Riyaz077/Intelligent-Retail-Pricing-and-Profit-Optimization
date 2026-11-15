import numpy as np
def make_features(df):
    x=df[["price","unit_cost","promotion","month"]].copy()
    x["gross_margin_rate"]=((x.price-x.unit_cost)/x.price.clip(lower=.01)).clip(-5,1)
    x["price_to_cost"]=x.price/x.unit_cost.clip(lower=.01)
    x["month_sin"]=np.sin(2*np.pi*x.month/12)
    x["month_cos"]=np.cos(2*np.pi*x.month/12)
    return x.replace([np.inf,-np.inf],0).fillna(0)
