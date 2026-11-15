import pandas as pd
from src.retailprofit.features import make_features
from src.retailprofit.pricing import estimate_elasticity
def test_margin_feature():
    x=make_features(pd.DataFrame([{"price":10.,"unit_cost":6.,"promotion":0,"month":1}]))
    assert round(x.iloc[0].gross_margin_rate,2)==.40
def test_negative_elasticity():
    d=pd.DataFrame({"price":[10,12,14,16,18,20,22,24,26,28,30,32],"units_sold":[100,90,82,75,69,64,59,55,51,48,45,42]})
    assert estimate_elasticity(d)<0
