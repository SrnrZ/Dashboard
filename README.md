📈 Bitcoin Price Prediction using the Prophet Model for Time Series


**Objective**
The goal of this project is to analyze and predict Bitcoin prices over time using Facebook's Prophet model for time series forecasting. We explore various forecasting models, ultimately selecting Prophet for its ability to handle seasonal and trend data effectively. The project also features an interactive Streamlit dashboard to visualize predictions and model insights.


**Dataset**
The dataset used for this project includes historical Bitcoin price data, covering essential features like date, price, and volume. We preprocess the data for time series analysis, import it into Prophet, and later incorporate global economic indicators to enhance the model's performance. The data is assumed to be in CSV format.


**Application of this Project**
Bitcoin price prediction is valuable for investors, researchers, and analysts seeking insights into potential future trends. With the Prophet model and Streamlit dashboard, this project delivers a user-friendly forecasting tool to visualize price predictions and facilitate more informed decision-making.


**Model Exploration and Refinement**
In this project, we experimented with multiple models before selecting the Prophet model. Here’s a summary of our exploration and findings:

AMRI Model: Initially, we tried the AMRI model for time series forecasting. However, it was not well-suited for Bitcoin’s high volatility. AMRI's reliance on moving average components made it more effective for slower-moving trends but inadequate for capturing Bitcoin's rapid fluctuations.

XGBoost: We then explored XGBoost, which requires substantial feature engineering. Despite efforts to create lag features, time-based variables (e.g., day of the week, seasonality), and rolling statistics, the model was highly prone to overfitting. It predicted the test data accurately but failed to generalize well to future data, especially under volatile conditions.

Prophet Model: Finally, we turned to the Prophet model, which performed well with Bitcoin’s seasonality and trends, delivering more robust forecasts. Prophet’s decomposition into trend, seasonality, and holiday effects made it a good fit for Bitcoin's price data.


**Streamlit Dashboard Setup**
To provide an interactive interface for users, we developed a Streamlit dashboard that enables real-time visualization of forecasts. Key steps included:

Setting up the Streamlit interface: We structured the interface to visualize price forecasts, trend analysis, and seasonal components.
Adding Global Liquidity as a Regressor: By incorporating global liquidity as an additional regressor, we aimed to capture broader economic influences. However, integrating regressors posed challenges:
Additional regressors require separate forecasting models and alignment with the main model.
Managing NaN values and ensuring overlap in time series data for consistent forecasting.


**Project Structure**
This project includes the following files:

main.ipynb - The primary notebook containing data loading, preprocessing, model training, and evaluation.
README.md - A detailed project overview, including objectives, dataset description, model experiments, and conclusions.
data_cleaning.ipynb - Outlines the data cleaning process, covering handling of missing values, outlier detection, and preprocessing for time series modeling.
streamlit_dashboard.py - The Streamlit dashboard code that enables interactive forecast visualization.


**Conclusion**
This project successfully leverages the Prophet model to predict Bitcoin price trends, and the Streamlit dashboard provides an accessible visualization interface. Our findings show that:

The Prophet model captures seasonality and trend components in Bitcoin prices effectively.
While adding additional economic indicators (e.g., global liquidity) enriches the model, it also introduces challenges, particularly with data alignment and NaN handling.
The project concludes with a well-tuned forecast model and a structured narrative in a presentation format.


**Key Learnings and Future Work**
Parameter Tuning: Fine-tuning parameters in Prophet allowed for more accurate predictions by adjusting seasonality and trend sensitivities.
Feature Integration: Adding external regressors like global liquidity enhanced our model’s economic context but required additional handling to align forecast periods.
User Interface: The Streamlit dashboard offers a dynamic way to explore and visualize forecasts, making the model accessible to non-technical users.


**Prerequisites**
Python (Jupyter Notebook and Streamlit)
Libraries: Prophet, pandas, matplotlib, numpy, Streamlit
GitHub Repository Link: [Your Repository Link Here]
