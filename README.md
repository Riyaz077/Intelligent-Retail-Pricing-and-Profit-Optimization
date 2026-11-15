# RetailProfit AI
## Intelligent Retail Pricing, Revenue and Profitability Optimization System

RetailProfit AI is a retail analytics demonstrator that combines demand modelling, price elasticity analysis, revenue and gross-profit simulation, and constrained price recommendations.

> The included dataset is synthetic. Results are illustrative and do not establish real-world pricing lift. Validate recommendations using real sales, cost, inventory, competitor, and promotion data.

### Features
- Retail sales data generation, validation, and exploratory analytics.
- Demand estimation using a Random Forest regression baseline.
- Pooled price elasticity estimation using log-log regression.
- Candidate price simulation for demand, revenue, and gross profit.
- Price floor, ceiling, and maximum-change constraints.
- Product-level recommendation table and Streamlit dashboard.
- FastAPI endpoint for pricing scenarios.
- Jupyter notebooks, tests, and technical documentation.

### Architecture
```text
Retail Sales Data -> Validation -> Feature Engineering
       -> Demand Model + Elasticity Analysis
       -> Price / Revenue / Profit Simulator
       -> Business Constraints -> Recommendations
       -> Streamlit Dashboard + FastAPI
```

### Stack
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Streamlit, FastAPI, Joblib, Pytest.

### Structure
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

### Quick start
```bash
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/generate_data.py
python scripts/run_pipeline.py
streamlit run dashboard/app.py
```
API:
```bash
uvicorn api.main:app --reload
```
Open `http://127.0.0.1:8000/docs`.

Tests:
```bash
pytest -q
```

### Methodology
1. Validate product-level price, cost, promotion, date, and sales data.
2. Engineer margin and seasonal features.
3. Train a demand regression model and evaluate MAE, RMSE, and R².
4. Estimate pooled log-log price elasticity.
5. Simulate candidate prices and calculate predicted units, revenue, and gross profit.
6. Apply price bounds and maximum-change constraints.
7. Rank recommendations and publish them through the dashboard and API.

### Optimization logic
Revenue = price × predicted units. Gross profit = (price − unit cost) × predicted units. The optimizer searches candidate prices within configurable bounds and selects the highest estimated gross-profit scenario. This is a decision-support baseline, not a dynamic pricing engine; it does not currently model inventory, competitor prices, substitution, or causal promotion effects.

### Responsible use and limitations
Avoid discriminatory or collusive pricing and comply with consumer-protection, competition, privacy, and sector-specific requirements. Synthetic data, pooled elasticity, and simplified demand features limit the reliability of recommendations. Validate pricing changes through controlled experiments before deployment.

### Author
**Mohamed Riyaz S.** | Computer Science & Engineering · Business Analytics

MIT License. See `LICENSE`.
