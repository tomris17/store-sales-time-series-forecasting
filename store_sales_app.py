import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Mağaza Satış Tahmin Uygulaması",
    page_icon="📈",
    layout="centered",
)


@st.cache_resource
def load_model():
  model = joblib.load("store_sales_gbm_model.pkl")
  columns = joblib.load("store_sales_columns.pkl")
  return model, columns


model, columns = load_model()

st.title("📈 Store Sales - Zaman Serisi Tahmin Sistemi")
st.write(
    "Bu uygulama, LightGBM modeli ile mağaza ve ürün ailesine göre satış"
    " tahmini yapar."
)

st.sidebar.header("Tahmin Parametreleri")

store_nbr = st.sidebar.selectbox(
    "Mağaza Numarası (store_nbr)", list(range(1, 55))
)
family = st.sidebar.selectbox(
    "Ürün Ailesi (family)",
    [
        "AUTOMOTIVE",
        "BABY CARE",
        "BEAUTY",
        "BEVERAGES",
        "BOOKS",
        "BREAD/BAKERY",
        "CELEBRATION",
        "CLEANING",
        "DAIRY",
        "DELI",
        "EGGS",
        "FROZEN FOODS",
        "GROCERY I",
        "GROCERY II",
        "HARDWARE",
        "HOME AND KITCHEN I",
        "HOME AND KITCHEN II",
        "HOME APPLIANCES",
        "LADIESWEAR",
        "LAWN AND GARDEN",
        "LINGERIE",
        "LIQUOR,WINE,BEER",
        "MEATS",
        "PERSONAL CARE",
        "PET SUPPLIES",
        "PLAYERS and ELECTRONICS",
        "POULTRY",
        "PREPARED FOODS",
        "PRODUCE",
        "SCHOOL AND OFFICE SUPPLIES",
        "SEAFOOD",
    ],
)
onpromotion = st.sidebar.checkbox("Promosyonda mı? (onpromotion)")
date = st.sidebar.date_input("Tahmin Tarihi", pd.to_datetime("2017-08-15"))

if st.sidebar.button("Satış Tahmini Yap"):
  input_df = pd.DataFrame(0, index=[0], columns=columns)

  day_of_week = date.dayofweek
  day_of_month = date.day
  month = date.month
  quarter = date.quarter
  year = date.year

  for col in input_df.columns:
    if "year" in col:
      input_df[col] = year
    elif "month" in col:
      input_df[col] = month
    elif "day_of_week" in col:
      input_df[col] = day_of_week
    elif "day_of_month" in col:
      input_df[col] = day_of_month
    elif "quarter" in col:
      input_df[col] = quarter
    elif "store_nbr" in col and str(store_nbr) in col:
      input_df[col] = 1
    elif "family" in col and family in col:
      input_df[col] = 1
    elif "onpromotion" in col:
      input_df[col] = int(onpromotion)

  pred_log = model.predict(input_df)[0]
  pred_sales = np.expm1(pred_log)
  if pred_sales < 0:
    pred_sales = 0

  st.success(f"### Tahmini Satış Miktarı: {pred_sales:,.2f} adet")