📈 Bitcoin Price Prediction using the Prophet Model for Time Series


**Objective**

The goal of this project is to provide comprehensive insights into Bitcoin's price trend by utilizing the Prophet Model for time series, while putting the Bitcoin price time series into context of its overall trend as well as seasonal (months, quarters, years) and cycle (accumulation, growth, bubble, crash) patterns. The project also features an interactive Streamlit dashboard to visualize predictions and model insights.


**Dataset**

The dataset used for this project includes historical Bitcoin price data retrieved from yahoo finance, covering essential features like date, price, and volume. Additionally, data published US Federal Reserves have been utilized to collect economic data such as e.g. global money supply (M2), federal interest rates and GDP growth rates. 


**Application of this Project**

Bitcoin price prediction is valuable for investors, researchers, and analysts seeking insights into potential future trends. With the Prophet model and Streamlit dashboard, this project delivers a user-friendly forecasting tool to visualize price predictions and facilitate more informed decision-making.


**Model Exploration and Refinement**

In this project, I experimented with multiple models before selecting the Prophet model. Here’s a summary of the exploration and findings:


AMRI Model: Initially, I tried the AMRI model for time series forecasting. However, it was not well-suited for Bitcoin’s high volatility. AMRI's reliance on moving average components made it more effective for slower-moving trends but inadequate for capturing Bitcoin's rapid fluctuations.


XGBoost: I then explored XGBoost, which requires substantial feature engineering. With making efforts to create lag features, time-based variables (e.g., day of the week, seasonality), and rolling statistics, the model highly proned to overfitting. It predicted the test data accurately but failed to generalize well to future data, especially under volatile conditions.


Prophet Model: Finally, I turned to the Prophet model, which performed well with Bitcoin’s seasonality and trends, delivering more robust forecasts. Prophet’s decomposition into trend, seasonality, and holiday effects made it a good fit for Bitcoin's price data. I also experimented with adding additional regressors, e.g. a times series for global liquidity, to capture broader economic influences. Additional regressors require separate forecasting models and alignment with the main model.


**Streamlit Dashboard Setup**

To provide an interactive interface for users, I developed a Streamlit dashboard that enables real-time (still on to do list) visualization of forecasts. Key features include current as well as projected (average, upper- and lower-bound) bitcoin price series, global liquidity time series as well as regulatory, halving and market top events.


**Project Structure**

This project includes the following files:

- prophet_btc.ipynb - The primary notebook containing data loading, preprocessing, model training, and evaluation.
- prophet_global_liquidity.ipynb - Notebook for modelling global liquidity
- README.md - A detailed project overview, including objectives, dataset description, model experiments, and conclusions.
- bitcoin_forecast_data.csv - Cleaned bitcoin price data set
- btc_forecast_app.py - The Streamlit dashboard code that enables interactive forecast visualization.


**Conclusion**

This project successfully leverages the Prophet model to predict Bitcoin price trends, and the Streamlit dashboard provides an accessible visualization interface. The findings show that:


- The Prophet model captures seasonality and trend components in Bitcoin prices effectively.
- It is crucial to correctly evaluate the timing of the current market cycle to reasonably adjust logistic's upper limit, trend changepoints and seasonality.
- While adding global liquidity as regressor to the model addresses a broader economic context, it's impact on the price forecast has been very little. Mainly due to global liquidity time series' high correlation (83%) to bitcoin price, global liquidity time series basically mirrors bitcoin's underlying price trend.
- The project concludes with a well-tuned forecast model and a structured narrative.


**Key Learnings and Future Work**

- Prophet Model: Not evrey model for making forecasts for time series data is suitable for highly and trending chart patterns. The prophet model seems to handle this challenge comparitvely well as it is decomposing the time series into several components (e.g. trend, seasons) that capture different aspects of the data and as a result automatically detects periodic patterns in the data. 
- Parameter Tuning: Fine-tuning parameters in Prophet allowed for more accurate predictions by adjusting seasonality and trend sensitivities.
- Feature Integration: Adding external regressors like global liquidity enhanced our model’s economic context but required additional handling to align forecast periods.
- User Interface: The Streamlit dashboard offers a dynamic way to explore and visualize forecasts, making the model accessible to non-technical users.


**Prerequisites**

Python (Jupyter Notebook and Streamlit)
Libraries: Prophet, pandas, matplotlib, numpy, Streamlit
