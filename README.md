# 🍷 Wine Sales Forecasting App

[![Streamlit App](https://img.shields.io/badge/Live%20App-Click%20Here-success?logo=streamlit)](https://timeserieswinesale-mbye5mjsegwbckbvv8txrg.streamlit.app/)
Deployed Live At:  
🔗 [https://timeserieswinesale-mbye5mjsegwbckbvv8txrg.streamlit.app/](https://timeserieswinesale-mbye5mjsegwbckbvv8txrg.streamlit.app/)

---

An interactive time series forecasting application for **Sparkling** and **Rose** wine sales using classical statistical models and deep learning techniques. This app allows users to explore model forecasts, residual diagnostics, and comparative model performance through an elegant Streamlit dashboard.

---

##  Key Features

-  Forecast wine sales using SARIMA, ARIMA, Prophet, LSTM, GRU, and more
-  Visualize residual diagnostics and stationarity transformations
-  Compare actual vs predicted across multiple models
-  Customize forecast horizon (1–12 months)
-  Deployed on Streamlit Cloud

---

##  Models Implemented

**Classical Statistical Models**
- Simple Average
- Moving Averages (2, 4, 6, 9-Point)
- Naive Baseline
- Regression (Linear)
- Simple, Double, and Triple Exponential Smoothing (Manual + Grid Search)

**ARIMA Family**
- Manual ARIMA: (2,1,1), (1,1,2), (2,1,3)
- Auto ARIMA
- SARIMA: (1,1,2)x(1,0,2,12), (0,1,2)x(2,0,2,12), Manual (3,1,2)(3,1,2,12)

**Other Forecasting Models**
- Facebook Prophet
- NeuralProphet (Experimental)
- XGBoost (with lag features)
- CNN-LSTM (deep learning sequence model)

---

##  Business Insights & Recommendations

###  Rose Wine – Key Takeaways
-  **Stable Forecasting Post-1982**: Residuals converge toward zero, indicating high reliability of forecasts in recent years.
-  **Inventory Planning**: Use SARIMA predictions to plan inventory cycles and avoid overstocking during low-sales months.
-  **Forecast Accuracy**: Minimal autocorrelation and normally distributed residuals confirm SARIMA assumptions are valid.
-  **Strategy Tip**: Avoid over-reliance on early launch data due to high variance. Focus on recent performance trends for marketing and demand planning.

###  Sparkling Wine – Key Takeaways
-  **High Volatility in Early Years**: Residuals show large fluctuations pre-1983; use caution when analyzing historical trends.
-  **Model Stabilization Over Time**: Post-1983 data shows tighter residuals and better forecasting accuracy.
-  **Sales & Promotions**: Plan promotions using post-1983 forecasts. Consider hybrid modeling with XGBoost for tighter predictions.
-  **Strategic Forecasting**: SARIMA can serve as a strong baseline model for monthly sales forecasting; combine with ML models during critical periods (e.g., holiday demand spikes).


---

##  Model Comparison Results

### **Sparkling Wine Forecasting Models**
| Model                                          | Train RMSE   | Train MAPE   |   Test RMSE |   Test MAPE | Data Source                       |
|------------------------------------------------|--------------|--------------|-------------|-------------|-----------------------------------|
| RegressionModel_Model1                         | 1279.32      | 40.05        |     1275.87 |       39.16 | original                          |
| Naive_Model2                                   | 3867.7       | 153.17       |     3864.28 |      152.87 | original                          |
| SimpleAveraging_Model3                         | 1298.48      | 40.36        |     1275.08 |       38.9  | original                          |
| 2-Point Trailing MA_Model4                     | 689.16       | 18.01        |      813.4  |       19.7  | original                          |
| 4-Point Trailing MA_Model4                     | 1106.4       | 34.28        |     1156.59 |       35.96 | original                          |
| 6-Point Trailing MA_Model4                     | 1261.79      | 42.11        |     1283.93 |       43.86 | original                          |
| 9-Point Trailing MA_Model4                     | 1372.84      | 45.99        |     1346.28 |       46.86 | original                          |
| SimpleExpSmoothing_Model5                      | 1317.13      | 39.05        |     1304.93 |       44.48 | original                          |
| SES_FixedAlpha=0.02_Model6                     | 1346.26      | 37.13        |     1278.5  |       40.71 | original                          |
| DoubleExpSmoothing_Alpha=0.65_Beta=0.0_Model7  | 1337.48      | 39.11        |     3851.44 |      152.08 | original                          |
| DES_GridSearch_Alpha=0.1_Beta=0.1_Model8       | 1363.47      | 44.26        |     1779.42 |       67.23 | original                          |
| TES_Auto_AddTrend_AddSeasonality_Model9        | 371.02       | 10.88        |      357.89 |       11.83 | original                          |
| TES_Final_Alpha=0.5_Beta=0.3_Gamma=0.4_Model10 | 477.4        | 14.36        |      649.2  |       21.59 | original                          |
| ARIMA_(2, 1, 2)_Model11                        | 1082.42      | 32.88        |     1299.98 |       43.2  | original data | 1st diff in Model |
| SARIMA_(1, 1, 2)_x_(1, 0, 2, 12)_Model12       | 592.29       | 15.04        |      528.59 |       18.89 | original data | 1st diff Model    |
| Manual_ARIMA_(2,1,1)_Model13                   | 1187.82      | 34.81        |     1274.94 |       38.65 | original data | 1st diff in Model |
| Manual_ARIMA_(1,1,2)_Model13                   | 1192.36      | 35.1         |     1274.37 |       38.55 | original data | 1st diff in Model |
| SARIMA_Manual_(3,1,2)(3,1,2,12)_Model14        | 641.92       | 16.27        |      329.53 |       10.36 | original data | 1st diff model    |
| Prophet_Model15                                |              |              |      440.63 |       14.35 | original | reindexed              |
| XGBoost_Model16                                | 79.5         | 2.57         |      441.33 |       13.19 | original | lag features           |
| CNN_LSTM_Model17                               | 447.29       | 14.74        |      437.75 |       12.95 | scaled + inverse                  |

---

### **Rose Wine Forecasting Models**
| Model                                          | Train RMSE   | Train MAPE   |   Test RMSE |   Test MAPE | Data Source                       |
|------------------------------------------------|--------------|--------------|-------------|-------------|-----------------------------------|
| RegressionModel_Model1                         | 30.72        | 21.22        |       51.39 |       91.49 | original                          |
| Naive_Model2                                   | 45.06        | 36.38        |       79.67 |      144.91 | original                          |
| SimpleAveraging_Model3                         | 36.03        | 25.39        |       53.41 |       94.77 | original                          |
| 2-Point Trailing MA_Model4                     | 19.47        | 12.47        |       11.53 |       13.57 | original                          |
| 4-Point Trailing MA_Model4                     | 25.97        | 18.03        |       14.44 |       19.46 | original                          |
| 6-Point Trailing MA_Model4                     | 28.46        | 20.41        |       14.55 |       20.82 | original                          |
| 9-Point Trailing MA_Model4                     | 30.23        | 22.06        |       14.72 |       20.99 | original                          |
| SimpleExpSmoothing_Model5                      | 31.78        | 22.37        |       37.54 |       65.2  | original                          |
| SES_FixedAlpha=0.07_Model6                     | 32.65        | 23.02        |       36.39 |       63.09 | original                          |
| DoubleExpSmoothing_Alpha=0.0_Beta=0.0_Model7   | 30.72        | 21.22        |       15.25 |       22.69 | original                          |
| DES_GridSearch_Alpha=0.1_Beta=0.1_Model8       | 32.03        | 22.78        |       37.01 |       63.89 | original                          |
| TES_Auto_AddTrend_AddSeasonality_Model9        | 19.48        | 13.27        |       14.23 |       19.16 | original                          |
| TES_Final_Alpha=0.3_Beta=0.3_Gamma=0.4_Model10 | 25.31        | 18.48        |       12.74 |       17.01 | original                          |
| ARIMA_(2, 1, 3)_Model11                        | 31.54        | 22.62        |       36.77 |       63.77 | original data | 1st diff in Model |
| SARIMA_(0, 1, 2)_x_(2, 0, 2, 12)_Model12       | 32.23        | 18.55        |       26.88 |       46.48 | original data | 1st diff Model    |
| Manual_ARIMA_(2,1,1)_Model13                   | 32.6         | 22.88        |       16.76 |       21.69 | original data | 1st diff in Model |
| SARIMA_Manual_(3,1,2)(3,1,2,12)_Model14        | 42.46        | 24.38        |       16.76 |       25.08 | original data | 1st diff model    |
| Prophet_Model15                                |              |              |       17.3  |       24.42 | original | reindexed              |
| XGBoost_Model16                                | 4.97         | 3.78         |       27.65 |       46.09 | original | lag features           |
| CNN_LSTM_Model17                               | 26.05        | 17.97        |       17.04 |       28.72 | scaled + inverse                  |

---

##  Folder Structure

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

##  How to Run Locally

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


##  Author

**Anmol Dwivedi**  
📍 Dallas, TX  
📧 dwivedi.anmol1996@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/anmol-dwivedi) | [GitHub](https://github.com/anmol-dwivedi) | [Portfolio](https://anmol-dwivedi-portfolio.netlify.app)

---

##  License

This project is open-source and free for academic and demonstration purposes.
