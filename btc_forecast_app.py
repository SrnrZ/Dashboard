import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from datetime import timedelta

# Page Config
st.set_page_config(layout="wide")

# Event type descriptions
event_type_info = {
    "Halving": "Bitcoin halving events occur approximately every four years, reducing the reward miners receive for validating blocks. This can lead to changes in the Bitcoin price due to reduced supply.",
    "Market Top": "Market Top and Bottom events refer to significant price fluctuations in the Bitcoin market, marking extreme highs (Tops) or lows (Bottoms) in value, often leading to market corrections.",
    "Regulation": "Since 2016, global regulatory progress on cryptocurrency has included Japan's recognition of crypto as legal payment, Malta, Dubai, and the EU establishing crypto frameworks, China's comprehensive ban, El Salvador and the Central African Republic adopting Bitcoin as legal tender, and recent approvals for Bitcoin ETFs in the U.S., marking a shift toward mainstream acceptance and oversight."
}

# Data set
forecast = pd.read_csv(".../bitcoin_forecast.csv", delimiter=';')
forecast['date'] = pd.to_datetime(forecast['date'], format='%d.%m.%Y')

# Displaying "Real" price data 
cutoff_date = pd.to_datetime('2024-11-12')
last_real_date = forecast[forecast['date'] <= cutoff_date]['date'].max()

if last_real_date < cutoff_date:
    last_real_value = forecast.loc[forecast['date'] == last_real_date, 'close'].values[0]
    additional_dates = pd.date_range(last_real_date + timedelta(days=1), cutoff_date)
    extended_real = pd.DataFrame({'date': additional_dates, 'close': last_real_value})
    forecast = pd.concat([forecast, extended_real], ignore_index=True)

# Sidebar section: Chart display options
st.sidebar.title("Chart Display Options")
show_forecast = st.sidebar.checkbox('BTC Price Forecast', value=False)
#show_scenario = st.sidebar.checkbox('Show Scenario Forecast', value=False)
show_global_liquidity = st.sidebar.checkbox('Global Liquidity', value=False)
show_forecast_bounds = st.sidebar.checkbox('BTC Price Forecast Bounds', value=False)
#show_scenario_bounds = st.sidebar.checkbox('Show Scenario Bounds', value=False)

# Events
events = [
    {"date": "2016-05-01", "event": "1", "type": "Regulation", "details": "Japan passed the Payment Services Act recognizing crypto as a legal payment method."},
    {"date": "2018-03-01", "event": "2", "type": "Regulation", "details": "Wyoming passed blockchain-friendly laws, establishing 'crypto valley'."},
    {"date": "2018-06-01", "event": "3", "type": "Regulation", "details": "SEC declares view that most cryptocurrencies are securities."},
    {"date": "2021-09-01", "event": "4", "type": "Regulation", "details": "El Salvador adopted Bitcoin as legal tender."},
    {"date": "2021-09-01", "event": "5", "type": "Regulation", "details": "China announces a comprehensive ban on crypto trading."},
    {"date": "2022-03-01", "event": "6", "type": "Regulation", "details": "Dubai established the Virtual Assets Regulatory Authority (VARA)."},
    {"date": "2022-04-01", "event": "7", "type": "Regulation", "details": "Central African Republic adopts Bitcoin as legal tender."},
    {"date": "2023-06-01", "event": "8", "type": "Regulation", "details": "Hong Kong implements new licensing regime for crypto exchanges."},
    {"date": "2024-01-01", "event": "9", "type": "Regulation", "details": "SEC approves spot Bitcoin ETFs for the first time."},
    {"date": "2016-07-09", "event": "BTC Halving", "type": "Halving", "details": "Second BTC Halving event, further reducing block rewards."},
    {"date": "2020-05-11", "event": "BTC Halving", "type": "Halving", "details": "Third BTC Halving event occurred, continuing to reduce block rewards."},
    {"date": "2024-04-08", "event": "BTC Halving", "type": "Halving", "details": "Upcoming BTC Halving event expected to reduce block rewards again."},
    {"date": "2017-12-17", "event": "518 d after halving (Top)\n+12300%", "type": "Market Top", "details": "BTC reached a market top with a 2070% increase."},
    {"date": "2021-11-10", "event": "539 d after halving (Top)\n+2070%", "type": "Market Top", "details": "BTC surged by 850% before reaching its peak."},
    {"date": "2025-09-25", "event": "530 d after halving\n(+?%)", "type": "Market Top"}
]

events_df = pd.DataFrame(events)
events_df['date'] = pd.to_datetime(events_df['date'])

# Sidebar: Event selection
event_types = events_df['type'].unique()
selected_event_types = st.sidebar.multiselect("BTC related Events", options=event_types, default=[])

# Additional information for selected event types displayed
st.sidebar.subheader("")
for event_type in selected_event_types:
    st.sidebar.markdown(f"**{event_type}**")
    st.sidebar.markdown(f"{event_type_info.get(event_type, 'No additional information available.')}", unsafe_allow_html=True)

# Event filters
filtered_events = events_df[events_df['type'].isin(selected_event_types)]

# Initialize Plotly figure
fig = go.Figure()

# Plot "Real" line (actual Bitcoin price)
fig.add_trace(go.Scatter(x=forecast[forecast['date'] <= cutoff_date]['date'], y=forecast[forecast['date'] <= cutoff_date]['close'], mode='lines', name='Real', line=dict(color='black')))

# Adding additional plot lines based on chart options 
if show_forecast:
    fig.add_trace(go.Scatter(x=forecast['date'], y=forecast['yhat'], mode='lines', name='Forecast', line=dict(color='red')))
#if show_scenario:
    #fig.add_trace(go.Scatter(x=forecast['date'], y=forecast['scenario'], mode='lines', name='Scenario Forecast', line=dict(color='orange')))
if show_forecast_bounds:
    fig.add_trace(go.Scatter(x=forecast['date'], y=forecast['yhat_lower'], mode='lines', name='Forecast Lower Bound', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=forecast['date'], y=forecast['yhat_upper'], mode='lines', name='Forecast Upper Bound', line=dict(color='green')))
#if show_scenario_bounds:
    #fig.add_trace(go.Scatter(x=forecast['date'], y=forecast['scenario_lower'], mode='lines', name='Scenario Lower Bound (S)', line=dict(color='yellow')))
    #fig.add_trace(go.Scatter(x=forecast['date'], y=forecast['scenario_upper'], mode='lines', name='Scenario Upper Bound (S)', line=dict(color='brown')))
if show_global_liquidity:
    fig.add_trace(go.Scatter(x=forecast['date'], y=forecast['global_liquidity'], mode='lines', name='Global Liquidity (bln)', line=dict(color='green')))

# Layout adjustments for expanded y-axis range if required
visible_max_y = max(
    forecast['close'].max(),
    forecast['yhat'].max() if show_forecast else 0,
    #forecast['scenario'].max() if show_scenario else 0,
    forecast['yhat_upper'].max() if show_forecast_bounds else 0,
    #forecast['scenario_upper'].max() if show_scenario_bounds else 0,
    forecast['global_liquidity'].max() if show_global_liquidity else 0
)

for idx, row in filtered_events.iterrows():
    label_y_pos = visible_max_y * 0.95 

    event_label = row['event'].replace("\n", "<br>")
    
    fig.add_trace(go.Scatter(
        x=[row['date']],
        y=[label_y_pos],
        text=event_label,
        mode='text',
        textposition="top center",
        textfont=dict(size=16)
    ))

    # Adding a vertical line to the event
    fig.add_shape(
        type="line",
        x0=row['date'],
        y0=label_y_pos * 0.95,
        x1=row['date'],
        y1=forecast.loc[forecast['date'] == row['date'], 'close'].values[0] if not forecast[forecast['date'] == row['date']].empty else 0,
        line=dict(color="purple", width=1, dash="dot")
    )

fig.update_layout(
    title="",
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    template="plotly_dark",
    width=1600,
    height=800,
    margin=dict(t=150)
)

# Displaying the figure in Streamlit
st.title("Bitcoin Price Chart")
st.plotly_chart(fig, use_container_width=True)

# Displaying regulation events list below the chart
if "Regulation" in selected_event_types:
    st.subheader("Regulation Events Timeline")
    regulation_events = events_df[events_df['type'] == 'Regulation'].sort_values('date')
    for _, event in regulation_events.iterrows():
        st.write(f"{event['event']}. {event['date'].strftime('%Y-%m-%d')}: {event['details']}")