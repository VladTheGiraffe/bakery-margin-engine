# Bakery Margin Engine

## 📋 Business Problem
Fluctuating raw material and commodity prices pose a direct threat to small business retail margins. This project provides commercial bakeries with an automated pricing engine that maps raw material fluctuations directly to item yields, ensuring micro-margins are protected through data-driven target retail pricing.

## 🛠️ Tech Stack & Infrastructure
- **Languages:** Python, SQL
- **Database:** PostgreSQL (Local Host Cluster)
- **Frameworks & Libraries:** Streamlit (UI), Pandas (Data Manipulation), `psycopg` (Database Connector)
- **Administration:** DBeaver (Schema Migrations & Query Analysis)

## 🗄️ Database Schema Design
The backend relies on a fully normalized 3-table relational architecture designed to eliminate data redundancy and enforce relational integrity:
- `ingredients`: Tracks raw material costs, units, and stock levels.
- `recipes`: Stores menu item metadata and target profit margins.
- `recipe_ingredients`: A bridge/junction table resolving the many-to-many relationship, tracking line-item ingredient quantities mapped per recipe.

## 🏗️ Execution Pipeline
1. **Database Connection:** Establishes a secure connection to the local PostgreSQL database using the `psycopg` adapter, reading connection strings dynamically via environment variables.
2. **Analytical Layer:** Executes optimized SQL `JOIN` queries to merge relational tables. Uses Pandas DataFrames to calculate total raw material costs, target item yields, and minimum sustainable retail prices on the fly.
3. **Frontend Presentation:** Powers an interactive, local Streamlit dashboard that renders live database queries into clean UI metric cards for real-time business decisions.

## 🚀 How to Run Locally
1. Ensure a local PostgreSQL instance is running with the schema applied.
2. Spin up the local interactive web server:
   
   streamlit run app.py

---
