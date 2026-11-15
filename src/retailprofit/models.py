import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
def train_demand_model(X,y):
    m=Pipeline([("imputer",SimpleImputer(strategy="median")),("model",RandomForestRegressor(n_estimators=180,min_samples_leaf=3,random_state=42,n_jobs=-1))])
    return m.fit(X,y)
def metrics(y,p):
    return {"MAE":float(mean_absolute_error(y,p)),"RMSE":float(np.sqrt(mean_squared_error(y,p))),"R2":float(r2_score(y,p))}
