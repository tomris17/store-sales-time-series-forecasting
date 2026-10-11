# 🛒 Store Sales - Time Series Forecasting

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Library-Pandas-orange.svg)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/Library-Scikit_Learn-yellow.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-red.svg)](https://streamlit.io/)

This repository contains an end-to-end time series forecasting solution for the **Kaggle Store Sales - Time Series Forecasting** competition. The objective is to predict unit sales for thousands of items sold at different Favorita stores located in Ecuador.

---

## 📊 Project Overview
* **Objective:** Build robust forecasting models to predict retail store sales over future time horizons (evaluated using Root Mean Squared Logarithmic Error - RMSLE).
* **Key Steps:**
  * Exploratory Data Analysis (EDA) on temporal sales patterns, seasonality, holidays, promotions, and oil prices.
  * Time-series Feature Engineering (lag features, rolling windows, calendar/date attributes).
  * Model Training using regression and gradient boosting models (e.g., LightGBM, XGBoost, or Random Forest).
  * Interactive web dashboard deployment via **Streamlit** to visualize sales trends and forecasts.

---

## 🛠️ Tech Stack & Libraries
* **Python**
* **Pandas & NumPy** (Time-series data manipulation & resampling)
* **Scikit-Learn & LightGBM** (Machine Learning Modeling)
* **Matplotlib & Seaborn** (Trend & Seasonality Visualizations)
* **Streamlit** (Interactive Dashboard)

---

## 🚀 Getting Started & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tomris17/store-sales-time-series-forecasting.git](https://github.com/tomris17/store-sales-time-series-forecasting.git)
   cd store-sales-time-series-forecasting
