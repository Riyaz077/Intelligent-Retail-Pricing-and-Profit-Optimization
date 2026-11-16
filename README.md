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

For your GitHub README, I recommend using a **Mermaid flowchart**. It looks professional, is easy to maintain, and renders directly on GitHub.

### **Architecture – System Workflow**

\#chatgpt-mermaid-\_r_n5\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_n5\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_n5\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_n5\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_n5\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_n5\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_n5\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_n5\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_n5\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_n5\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_n5\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_n5\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_n5\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_n5\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_n5\_ p{margin:0;}#chatgpt-mermaid-\_r_n5\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_n5\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_n5\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_n5\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_n5\_ .label text,#chatgpt-mermaid-\_r_n5\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_n5\_ .node rect,#chatgpt-mermaid-\_r_n5\_ .node circle,#chatgpt-mermaid-\_r_n5\_ .node ellipse,#chatgpt-mermaid-\_r_n5\_ .node polygon,#chatgpt-mermaid-\_r_n5\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_n5\_ .rough-node .label text,#chatgpt-mermaid-\_r_n5\_ .node .label text,#chatgpt-mermaid-\_r_n5\_ .image-shape .label,#chatgpt-mermaid-\_r_n5\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_n5\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_n5\_ .rough-node .label,#chatgpt-mermaid-\_r_n5\_ .node .label,#chatgpt-mermaid-\_r_n5\_ .image-shape .label,#chatgpt-mermaid-\_r_n5\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_n5\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_n5\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_n5\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_n5\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_n5\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_n5\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_n5\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_n5\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_n5\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_n5\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_n5\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_n5\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_n5\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_n5\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_n5\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_n5\_ .icon-shape,#chatgpt-mermaid-\_r_n5\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_n5\_ .icon-shape p,#chatgpt-mermaid-\_r_n5\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_n5\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_n5\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_n5\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_n5\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_n5\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_n5\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_n5\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_n5\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_n5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_n5\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_n5\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_n5\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_n5\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_n5\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_n5\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_n5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_n5\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_n5\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_n5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_n5\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_n5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_n5\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_n5\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_n5\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_n5\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_n5\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_n5\_ .node rect,#chatgpt-mermaid-\_r_n5\_ .node circle,#chatgpt-mermaid-\_r_n5\_ .node ellipse,#chatgpt-mermaid-\_r_n5\_ .node polygon,#chatgpt-mermaid-\_r_n5\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_n5\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_n5\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_n5\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_n5\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_n5\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}📊 Retail Sales DatasetData Validation & QualityChecksData Preprocessing & FeatureEngineeringDemand Forecasting ModelPrice Elasticity AnalysisPrice Optimization EngineRevenue & Profit SimulationBusiness Constraints &OptimizationAI-Driven PricingRecommendationsInteractive StreamlitDashboardFastAPI Prediction ServicesBusiness Insights &VisualizationAPI-Based Integration

**Workflow overview:**

1. **Data Layer:** Collect and validate retail sales data.
2. **Analytics Layer:** Perform feature engineering, demand forecasting, and price elasticity analysis.
3. **Optimization Layer:** Simulate pricing scenarios and evaluate revenue, profit, and business constraints.
4. **Decision Layer:** Generate AI-driven pricing recommendations.
5. **Application Layer:** Deliver insights through Streamlit and FastAPI.

**GitHub tip:** Use the Mermaid code directly inside your README.md. GitHub automatically renders it as an interactive-style architecture diagram.

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

**Mohamed Riyaz S.**  
Integrated M.Tech, Computer Science and Engineering (Business Analytics)  
VIT Chennai
