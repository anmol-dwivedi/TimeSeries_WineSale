# 🍷 Wine Sales Forecasting App

[![Streamlit App](https://img.shields.io/badge/Live%20App-Click%20Here-success?logo=streamlit)](https://timeserieswinesale-mbye5mjsegwbckbvv8txrg.streamlit.app/)

An interactive time series forecasting application for **Sparkling** and **Rose** wine sales using classical statistical models and deep learning techniques. This app allows users to explore model forecasts, residual diagnostics, and comparative model performance through an elegant Streamlit dashboard.

---

## 🚀 Key Features

- 🔮 Forecast wine sales using SARIMA, ARIMA, Prophet, LSTM, GRU, and more
- 📊 Visualize residual diagnostics and stationarity transformations
- 🔄 Compare actual vs predicted across multiple models
- 📈 Customize forecast horizon (1–12 months)
- 🌐 Deployed on Streamlit Cloud

---

## 🧠 Models Implemented

| Model Type       | Technique |
|------------------|-----------|
| Statistical      | ARIMA (manual + auto), SARIMA, Exponential Smoothing |
| ML/DL            | LSTM, GRU, NeuralProphet |
| Forecasting APIs | Facebook Prophet |

---

## 🗂️ Folder Structure

```
TimeSeries_WineSale/
├── Deployment/
│   ├── app.py
│   ├── Sparkling.csv
│   ├── Rose.csv
│   ├── sparkling_sarima_model.pkl
│   ├── rose_sarima_model.pkl
│   ├── Sparkling SARIMA Model Plot Diagnostics.png
│   ├── Rose_SARIMA_Model_Diagnostics.png
│   ├── ResidualsOverTime-Sparkling.png
│   ├── ResidualsOverTime-Rose.png
│   ├── Rolling Residual Diagnostics-Sparkling.png
│   ├── RollingResidualDiagnostics-Rose.png
│   ├── sparkling_model_plot_data.csv
│   └── rose_model_plot_data.csv
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/anmol-dwivedi/TimeSeries_WineSale.git
cd TimeSeries_WineSale

# 2. Create environment and install dependencies
conda create -n wineforecast python=3.10
conda activate wineforecast
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run Deployment/app.py
```

---

## 📈 Streamlit App Preview

Deployed Live At:  
🔗 [https://timeserieswinesale-mbye5mjsegwbckbvv8txrg.streamlit.app/](https://timeserieswinesale-mbye5mjsegwbckbvv8txrg.streamlit.app/)

---

## 👨‍💻 Author

**Anmol Dwivedi**  
📍 Dallas, TX  
📧 dwivedi.anmol1996@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/anmol-dwivedi) | [GitHub](https://github.com/anmol-dwivedi) | [Portfolio](https://anmol-dwivedi-portfolio.netlify.app)

---

## 🧾 License

This project is open-source and free for academic and demonstration purposes.