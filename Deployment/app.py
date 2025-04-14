import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import joblib
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(layout="wide", page_title="Wine Sales Prediction App", page_icon="🍷")

# ---- Page Title ----
st.title("🍷 Wine Sales Prediction App")

# ---- Wine Selection ----
st.markdown("### Select Wine Type:")

col1, col2 = st.columns(2)

# Set default to Sparkling
if "wine" not in st.session_state:
    st.session_state["wine"] = "Sparkling"

with col1:
    if st.button("🍾 Sparkling Wine Data", use_container_width=True):
        st.session_state["wine"] = "Sparkling"

with col2:
    if st.button("🌹 Rose Data", use_container_width=True):
        st.session_state["wine"] = "Rose"

# Display selected wine
selected_wine = st.session_state["wine"]
st.markdown(f"**You selected:** {selected_wine} Wine Data")

# ---- Forecast Slider ----
st.markdown("---")
st.title("📆 Show me the forecast for the following months")
forecast_steps = st.slider("Months", 1, 12, 6)

# ---- Forecast Function ----
def get_sarima_forecast_plot(wine_type='Sparkling', forecast_steps=12):
    data_path = f'../Data/{wine_type}.csv'
    model_path = f'../{wine_type.lower()}_sarima_model.pkl'

    # Load dataset
    df = pd.read_csv(data_path, parse_dates=True)
    df['YearMonth'] = pd.to_datetime(df['YearMonth'], format='%Y-%m')
    df = df.set_index('YearMonth')
    df = df.asfreq('MS')

    if wine_type.lower() == 'rose':
        df[wine_type] = df[wine_type].interpolate(method='spline', order=1)

    # Load model
    model = joblib.load(model_path)

    # Forecast
    forecast_df = model.get_forecast(steps=forecast_steps).summary_frame(alpha=0.05)

    # Plot with Plotly
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df.index, y=df[wine_type],
        mode='lines+markers',
        name='Observed',
        line=dict(color='blue')
    ))

    fig.add_trace(go.Scatter(
        x=forecast_df.index, y=forecast_df['mean'],
        mode='lines+markers',
        name='Forecast',
        line=dict(color='red', dash='dash')
    ))

    fig.add_trace(go.Scatter(
        x=forecast_df.index.tolist() + forecast_df.index[::-1].tolist(),
        y=forecast_df['mean_ci_upper'].tolist() + forecast_df['mean_ci_lower'][::-1].tolist(),
        fill='toself',
        fillcolor='rgba(255,0,0,0.1)',
        line=dict(color='rgba(255,255,255,0)'),
        hoverinfo="skip",
        showlegend=True,
        name="Confidence Interval"
    ))

    fig.update_layout(
        title=f"Final Forecast using SARIMA - {wine_type} Wine",
        xaxis_title="Date",
        yaxis_title=wine_type,
        template="plotly_white",
        width=900,
        height=500
    )

    return fig

# ---- Show Forecast Plot ----
fig = get_sarima_forecast_plot(
    wine_type=selected_wine,
    forecast_steps=forecast_steps
)
st.plotly_chart(fig, use_container_width=True)

# ---- Diagnostics Section ----
st.markdown("---")
col1, col2 = st.columns([2, 2], gap="large")

# LEFT SIDE → SARIMA Diagnostics Image
with col1:
    st.subheader("🧪 Summary Diagnostic Plots from SARIMA")
    if selected_wine.lower() == "rose":
        sarima_img = "Rose_SARIMA_Model_Diagnostics.png"
    else:
        sarima_img = "Sparkling SARIMA Model Plot Diagnostics.png"
    st.image(f"./{sarima_img}", use_container_width=True)

# RIGHT SIDE → Residual & Rolling Residual Images
with col2:
    st.subheader("📈 Residual Over Time Plot")
    if selected_wine.lower() == "rose":
        residual_img = "ResidualsOverTime-Rose.png"
    else:
        residual_img = "ResidualsOverTime-Sparkling.png"
    st.image(f"./{residual_img}", use_container_width=True)

    st.subheader("🔁 Rolling Residual Diagnostics Plot")
    if selected_wine.lower() == "rose":
        rolling_img = "RollingResidualDiagnostics-Rose.png"
    else:
        rolling_img = "Rolling Residual Diagnostics-Sparkling.png"
    st.image(f"./{rolling_img}", use_container_width=True)
