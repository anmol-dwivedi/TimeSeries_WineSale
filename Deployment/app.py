import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="Wine Sales Prediction App", page_icon="🍷")

# ---- Page Title ----
st.title("🍷 Wine Sales Prediction App")

# ---- Wine Selection ----
st.markdown("### Select Wine Type:")
col1, col2 = st.columns(2)
if "wine" not in st.session_state:
    st.session_state["wine"] = "Sparkling"

with col1:
    if st.button("🍾 Sparkling Wine Data", use_container_width=True):
        st.session_state["wine"] = "Sparkling"
with col2:
    if st.button("🌹 Rose Data", use_container_width=True):
        st.session_state["wine"] = "Rose"

selected_wine = st.session_state["wine"]
st.markdown(f"**You selected:** {selected_wine} Wine Data")

# ---- Forecast Slider ----
st.markdown("---")
st.title("📆 Show me the forecast for the following months")
forecast_steps = st.slider("Months", 1, 12, 6)

# ---- Forecast Function ----
def get_sarima_forecast_plot(wine_type='Sparkling', forecast_steps=12):
    data_path = f"Deployment/{wine_type}.csv"
    model_path = f"Deployment/{wine_type.lower()}_sarima_model.pkl"
    df = pd.read_csv(data_path, parse_dates=True)
    df['YearMonth'] = pd.to_datetime(df['YearMonth'], format='%Y-%m')
    df = df.set_index('YearMonth').asfreq('MS')

    if wine_type.lower() == 'rose':
        df[wine_type] = df[wine_type].interpolate(method='spline', order=1)

    model = joblib.load(model_path)
    forecast_df = model.get_forecast(steps=forecast_steps).summary_frame(alpha=0.05)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index, y=df[wine_type], mode='lines+markers', name='Observed',
        line=dict(color='#4682B4', width=2.5)))
    fig.add_trace(go.Scatter(
        x=forecast_df.index, y=forecast_df['mean'], mode='lines+markers', name='Forecast',
        line=dict(color='crimson', dash='dash', width=2.5)))
    fig.add_trace(go.Scatter(
        x=forecast_df.index.tolist() + forecast_df.index[::-1].tolist(),
        y=forecast_df['mean_ci_upper'].tolist() + forecast_df['mean_ci_lower'][::-1].tolist(),
        fill='toself', fillcolor='rgba(200, 200, 200, 0.2)',
        line=dict(color='rgba(160, 160, 160, 0.5)', dash='dot'),
        hoverinfo="skip", showlegend=True, name="Confidence Interval"
    ))

    fig.update_layout(
        title=f"Forecast using SARIMA - {wine_type} Wine",
        xaxis_title="Date", yaxis_title="Wine Sales",
        template="plotly_white", height=600,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

# ---- Show Forecast Plot ----
fig = get_sarima_forecast_plot(wine_type=selected_wine, forecast_steps=forecast_steps)
st.plotly_chart(fig, use_container_width=True)

# ---- Diagnostics Section ----
st.markdown("---")
col1, col2 = st.columns([2, 2], gap="large")

with col1:
    st.subheader("🧪 Summary Diagnostic Plots from SARIMA")
    sarima_img = "Rose_SARIMA_Model_Diagnostics.png" if selected_wine == "Rose" else "Sparkling SARIMA Model Plot Diagnostics.png"
    st.image(f"Deployment/{sarima_img}", use_container_width=True)

with col2:
    st.subheader("📈 Residual Over Time Plot")
    residual_img = f"Deployment/ResidualsOverTime-{selected_wine}.png"
    st.image(residual_img, use_container_width=True)

    st.subheader("🔁 Rolling Residual Diagnostics Plot")
    rolling_img = f"Deployment/RollingResidualDiagnostics-Rose.png" if selected_wine == "Rose" else "Deployment/Rolling Residual Diagnostics-Sparkling.png"
    st.image(rolling_img, use_container_width=True)

# ---- Interpretation Section ----
st.markdown("---")
st.subheader(f"📘 Interpretation of Diagnostic Plots ({selected_wine} Wine)")
col1, col2, col3 = st.columns(3)

if selected_wine == "Rose":
    with col1:
        st.markdown("""
        **🧪 Summary Diagnostics (Top Left Panel):**
        - Residuals are centered around zero → no consistent over/under-prediction.
        - Histogram & Q-Q plot confirm residuals are approximately normally distributed.
        - Correlogram (ACF) shows no major autocorrelation → stable residual behavior.
        """)
    with col2:
        st.markdown("""
        **📈 Residuals Over Time (Top Right Panel):**
        - Errors fluctuate randomly → good model fit.
        - No drift or trend → seasonality captured well.
        - Spikes = potential anomalies worth exploring.
        """)
    with col3:
        st.markdown("""
        **🔁 Rolling Residual Diagnostics (Bottom Panel):**
        - Rolling mean stays flat → no bias buildup.
        - Residuals remain within ±2 std dev → accurate & consistent predictions.
        """)
else:
    with col1:
        st.markdown("""
        **🧪 Summary Diagnostics (Top Left Panel):**
        - Residuals centered around zero with low autocorrelation.
        - Histogram + Q-Q plot show normal distribution — model assumptions hold.
        """)
    with col2:
        st.markdown("""
        **📈 Residuals Over Time (Top Right Panel):**
        - No consistent pattern or upward/downward trend.
        - Indicates stable prediction over time.
        """)
    with col3:
        st.markdown("""
        **🔁 Rolling Residual Diagnostics (Bottom Panel):**
        - Errors mostly stay within ±2 std dev.
        - Confirms consistent model accuracy across time.
        """)

# ---- Model Comparison Section ----
st.markdown("---")
st.title("📊 Model Comparison: Actual vs Forecasts")

def load_comparison_data(csv_path):
    df = pd.read_csv(csv_path, parse_dates=["YearMonth"])
    df.set_index("YearMonth", inplace=True)
    return df

def get_model_name_map():
    return {
        "TES": "Triple Exponential Smoothing Tuned",
        "SARIMA": "Seasonal ARIMA",
        "Prophet": "Facebook Prophet",
        "ARIMA": "ARIMA",
        "LSTM": "LSTM Neural Net",
        "GRU": "GRU Neural Net",
        "Naive model": "Naive Forecast",
        "Regression": "Linear Regression",
        "Moving Average _2": "2 Month Moving Avg",
        "Moving Average _4": "4 Month Moving Avg",
        "Moving Average _6": "6 Month Moving Avg",
        "Moving Average _9": "9 Month Moving Avg",
        "Simple_average": "Simple Average",
        "Double_exponential_smoothing": "Double Exp Smoothing",
        "Simple_exponential_smoothing": "Simple Exp Smoothing",
        "Tes_auto": "Triple Exponential Smoothing (Auto)",
        "Tes_optimized": "Triple Exponential Smoothing (Optimized)",
        "Best_des": "Best Double Exponential Smoothing",
        "Arima_auto": "ARIMA (Auto)",
        "Arima_1_2": "ARIMA(1,2)",
        "Arima_2_1_1": "ARIMA(2,1,1)",
        "Sarima_3_1_2x3_1_2_12": "SARIMA Config A"
    }

model_name_map = get_model_name_map()
csv_path = f"Deployment/{selected_wine.lower()}_model_plot_data.csv"
df = load_comparison_data(csv_path)
available_models = [col for col in df.columns if col != "Actual"]

if "selected_models" not in st.session_state:
    st.session_state.selected_models = available_models[:5]

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("✅ Select All"):
        st.session_state.selected_models = available_models.copy()
with col2:
    if st.button("❌ Clear All"):
        st.session_state.selected_models = []

selected_model_keys = st.multiselect(
    "🔎 Select Models to Display:",
    options=available_models,
    default=st.session_state.selected_models,
    format_func=lambda x: model_name_map.get(x, x),
    key="model_picker"
)
st.session_state.selected_models = selected_model_keys

if selected_model_keys:
    st.markdown("#### ✅ Selected Models:")
    display_names = [model_name_map.get(k, k) for k in selected_model_keys]

    html_chips = """
    <style>
    .chip-container {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 10px;
    }
    .chip {
        background-color: #d9f3f1;
        border-radius: 20px;
        padding: 8px 16px;
        font-size: 14px;
        font-weight: 600;
        color: #004d40;
        box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
        min-width: 120px;
        text-align: center;
        transition: all 0.2s ease-in-out;
    }
    .chip:hover {
        background-color: #c2ece8;
        transform: scale(1.02);
    }
    </style>
    <div class="chip-container">
    """
    for name in display_names:
        html_chips += f"<div class='chip'>{name}</div>"
    html_chips += "</div>"
    st.markdown(html_chips, unsafe_allow_html=True)

# ---- Final Comparison Plot ----
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df.index, y=df["Actual"], mode="lines+markers", name="Actual",
    line=dict(color="crimson", width=3)))

for model_key in selected_model_keys:
    fig.add_trace(go.Scatter(
        x=df.index, y=df[model_key], mode="lines",
        name=model_name_map.get(model_key, model_key)
    ))

fig.update_layout(
    title=f"{selected_wine} Wine - Model Comparison vs Actual",
    xaxis_title="Date", yaxis_title="Wine Sales",
    template="plotly_white", height=600
)
st.plotly_chart(fig, use_container_width=True)
