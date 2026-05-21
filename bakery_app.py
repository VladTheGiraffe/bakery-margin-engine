import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import psycopg

load_dotenv()

# Connect to Database
DB_CONN = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
# Fetch the Data
@st.cache_data
def load_data(query, query_params):
    try:
        print("1. Attempting to connect to the database...")
        with psycopg.connect(DB_CONN) as conn:
            print("2. Connection Successful! Handing off to Pandas...")
            df = pd.read_sql_query(query, conn, params=query_params)
            print("3. Pandas finished the query! Returning data...")
            return df
    except Exception as e:
        print(f"FAILED: {e}")
        st.error(f"Database error: {e}")
        return pd.DataFrame()

#SQL
test_query = """
SELECT 
    ingredients.ingredient, 
    recipes.product, 
    recipe_ingredients.quantity, 
    ingredients.base_unit,
    ROUND((recipe_ingredients.quantity * ingredients.cost_per_unit), 2) AS line_item_cost
FROM recipe_ingredients
JOIN ingredients ON recipe_ingredients.item_id = ingredients.item_id
JOIN recipes ON recipe_ingredients.recipe_id = recipes.recipe_id
WHERE recipes.product = %s;
"""

#Frontend
st.title("Bakery Margin Engine")

menu_options = ["Bacon Breakfast Casserole: 1/2 Steam Pan", "Cinnamon Roll: Single", "Chicken Salad Sandwich on Croissant",
                "Yellow Cake with Buttercream Icing: 1/4 Sheet Pan", "Single Entree Buffet", "Pulled Pork: Pound", "Iced Tea: Gallon", 
                "Macaroni and Cheese: Large Side", "Garden Salad with Dressing: Regular Side", "Texas Sheet Cake: Large", "Potato Chips"]
selected_item = st.selectbox("Select a Menu Item to Analyze:", menu_options)

pantry_df = load_data(test_query, (selected_item,))
st.write(pantry_df)
total_cost = pantry_df['line_item_cost'].sum()
retail_price = st.number_input(
    f"Set Target Retail Price for {selected_item} ($):",
    min_value=0.00,
    value=10.00,
    step=0.50,
    format="%.2f"
)
gross_profit = retail_price - total_cost
gross_margin = ((retail_price - total_cost) / retail_price) * 100 if retail_price > 0 else 0 

st.subheader(f"Profitability Summary: {selected_item}")
col1, col2, col3 = st.columns(3)
col1.metric("Retail Price", f"${retail_price:.2f}")
col2.metric("Total Raw Cost", f"${total_cost:.2f}")
col3.metric("Gross Profit", f"${gross_profit:.2f}", delta=f"{gross_margin:.1f}%")

st.write("### Recipe Breakdown")
st.dataframe(pantry_df)