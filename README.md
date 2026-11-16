# RetailProfit AI
## Intelligent Retail Pricing, Revenue and Profitability Optimization System

RetailProfit AI is a retail analytics demonstrator that combines demand modelling, price elasticity analysis, revenue and gross-profit simulation, and constrained price recommendations.

> The included dataset is synthetic. Results are illustrative and do not establish real-world pricing lift. Validate recommendations using real sales, cost, inventory, competitor, and promotion data.

## **Features**
- Retail sales data generation, validation, and exploratory analytics.
- Demand estimation using a Random Forest regression baseline.
- Pooled price elasticity estimation using log-log regression.
- Candidate price simulation for demand, revenue, and gross profit.
- Price floor, ceiling, and maximum-change constraints.
- Product-level recommendation table and Streamlit dashboard.
- FastAPI endpoint for pricing scenarios.
- Jupyter notebooks, tests, and technical documentation.

For your GitHub README, I recommend using a **Mermaid flowchart**. It looks professional, is easy to maintain, and renders directly on GitHub.

## **Architecture – System Workflow**

                 ┌──────────────────────────┐
                 │    Retail Sales Data     │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │   Data Validation &     │
                 │   Preprocessing         │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │   Feature Engineering   │
                 └────────────┬─────────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
          ┌─────────────────┐  ┌─────────────────┐
          │ Demand          │  │ Price Elasticity│
          │ Forecasting    │  │ Analysis        │
          └────────┬────────┘  └────────┬────────┘
                   │                    │
                   └──────────┬─────────┘
                              ▼
                 ┌──────────────────────────┐
                 │  Price Optimization      │
                 │  & Scenario Simulation   │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ Revenue & Profit Analysis│
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ Business Constraints &   │
                 │ Optimization             │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ AI-Driven Pricing        │
                 │ Recommendations          │
                 └────────────┬─────────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
          ┌─────────────────┐  ┌─────────────────┐
          │ Streamlit       │  │ FastAPI         │
          │ Dashboard       │  │ Backend         │
          └────────┬────────┘  └────────┬────────┘
                   │                    │
                   ▼                    ▼
          ┌─────────────────┐  ┌─────────────────┐
          │ Business        │  │ API-Based       │
          │ Insights        │  │ Integration     │
          └─────────────────┘  └─────────────────┘
 
**Workflow overview:**

1. **Data Layer:** Collect and validate retail sales data.
2. **Analytics Layer:** Perform feature engineering, demand forecasting, and price elasticity analysis.
3. **Optimization Layer:** Simulate pricing scenarios and evaluate revenue, profit, and business constraints.
4. **Decision Layer:** Generate AI-driven pricing recommendations.
5. **Application Layer:** Deliver insights through Streamlit and FastAPI.

**GitHub tip:** Use the Mermaid code directly inside your README.md. GitHub automatically renders it as an interactive-style architecture diagram.

## **Stack**
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Streamlit, FastAPI, Joblib, Pytest.

## **Structure**
```text
RetailProfitAI/
├── api/                 # FastAPI service
├── config/              # Configuration
├── dashboard/           # Streamlit dashboard
├── data/sample/         # Synthetic retail dataset
├── docs/                # 20 technical documents
├── notebooks/           # 5 analysis notebooks
├── scripts/             # Data generation and training
├── src/retailprofit/    # Core ML and optimization logic
├── tests/
├── README.md
├── requirements.txt
└── LICENSE
```

## **Quick Start**

- Create and activate a Python virtual environment.
- Install all required dependencies from `requirements.txt`.
- Generate the sample dataset using the data generation script.
- Execute the end-to-end pipeline for data preprocessing, model training, and evaluation.
- Launch the Streamlit dashboard to explore interactive analytics and visualizations.
- Start the FastAPI backend to enable API-based model access.
- Access interactive API documentation at `http://127.0.0.1:8000/docs`.
- Run automated tests using `pytest -q` to validate project functionality.

## **Methodology**
1. Validate product-level price, cost, promotion, date, and sales data.
2. Engineer margin and seasonal features.
3. Train a demand regression model and evaluate MAE, RMSE, and R².
4. Estimate pooled log-log price elasticity.
5. Simulate candidate prices and calculate predicted units, revenue, and gross profit.
6. Apply price bounds and maximum-change constraints.
7. Rank recommendations and publish them through the dashboard and API.

## **Optimization logic**
Revenue = price × predicted units. Gross profit = (price − unit cost) × predicted units. The optimizer searches candidate prices within configurable bounds and selects the highest estimated gross-profit scenario. This is a decision-support baseline, not a dynamic pricing engine; it does not currently model inventory, competitor prices, substitution, or causal promotion effects.

## **Responsible use and limitations**
Avoid discriminatory or collusive pricing and comply with consumer-protection, competition, privacy, and sector-specific requirements. Synthetic data, pooled elasticity, and simplified demand features limit the reliability of recommendations. Validate pricing changes through controlled experiments before deployment.

## **Author**

**Mohamed Riyaz S.**  
Integrated M.Tech, Computer Science and Engineering (Business Analytics)  
VIT Chennai
