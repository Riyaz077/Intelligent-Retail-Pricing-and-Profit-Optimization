from pathlib import Path
import pandas as pd,streamlit as st
st.set_page_config(page_title="RetailProfit AI",page_icon="📈",layout="wide")
st.title("RetailProfit AI"); st.caption("Intelligent Retail Pricing, Revenue and Profitability Optimization")
p=Path("data/processed/pricing_recommendations.csv")
if not p.exists(): st.warning("Run python scripts/run_pipeline.py first."); st.stop()
sales=pd.read_csv("data/sample/retail_sales.csv"); rec=pd.read_csv(p)
rev=(sales.price*sales.units_sold).sum(); gp=((sales.price-sales.unit_cost)*sales.units_sold).sum()
a,b,c,d=st.columns(4); a.metric("Sales records",f"{len(sales):,}"); b.metric("Products",sales.product_id.nunique()); c.metric("Historical revenue",f"{rev:,.0f}"); d.metric("Gross profit",f"{gp:,.0f}")
t1,t2=st.tabs(["Sales Analytics","Pricing Recommendations"])
with t1:
    daily=sales.assign(revenue=sales.price*sales.units_sold).groupby("date").revenue.sum()
    st.line_chart(daily); st.bar_chart(sales.groupby("category").apply(lambda x:((x.price-x.unit_cost)*x.units_sold).sum(),include_groups=False))
with t2:
    st.dataframe(rec.sort_values("expected_gross_profit",ascending=False),use_container_width=True)
    sku=st.selectbox("Product",rec.product_id.tolist()); st.write(rec[rec.product_id==sku].T)
st.caption("Synthetic-data demonstrator; validate recommendations with controlled experiments.")
