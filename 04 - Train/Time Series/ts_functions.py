import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller, kpss
import warnings

def all_ac(Y, lags=15):
    """
    Plots the Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) for a time series.

    Parameters:
    Y (pd.Series): Time series.
    lags (int): Number of lags to plot. Default is 15.
    """
    fig, ax = plt.subplots(1, 2, figsize=(16, 5))
    plot_acf(Y, zero=False, ax=ax[0], lags=lags)
    ax[0].set_title('ACF')
    plot_pacf(Y, zero=False, ax=ax[1], lags=lags)
    ax[1].set_title('PACF')
    plt.show()

def plot_forecast(original_series, forecast):
    """
    Plots the historical series and the forecast.

    Parameters:
    original_series (pd.Series): Original time series.
    forecast (pd.Series): Forecasted time series.
    """
    plt.plot(original_series, label='Historical Series', linestyle='-')
    plt.plot(forecast, label='Forecast', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.title('Historical Series with Forecast')
    plt.legend()
    plt.show()

def stationarity_tests(s):
    """
    Performs KPSS and ADF stationarity tests on a time series.

    Parameters:
    s (pd.Series): Time series to be tested.

    Returns:
    tuple: Results of the KPSS and ADF tests ('Stationary' or 'Non-Stationary').
    """
    warnings.simplefilter("ignore", category=UserWarning)
    kps = kpss(s)
    adf = adfuller(s)
    warnings.simplefilter("default", category=UserWarning)
    kpss_pv, adf_pv = kps[1], adf[1]
    kpss_result, adf_result = 'Stationary', 'Non-Stationary'
    if adf_pv < 0.05:
        adf_result = 'Stationary'
    if kpss_pv < 0.05:
        kpss_result = 'Non-Stationary'
    return (kpss_result, adf_result)

def diagnostic(model, lags=15):
    """
    Plots the model diagnostics and the autocorrelation functions of the residuals.

    Parameters:
    model (statsmodels.tsa.arima.model.ARIMAResults): Fitted model.
    lags (int): Number of lags to plot. Default is 15.
    """
    print(model.summary())
    model.plot_diagnostics()
    plt.show()
    residuals = model.resid
    residuals = residuals[1:]
    all_ac(residuals, lags=lags)
    plt.show()

def compare_forecasts(original_series, forecast_list, model_list):
    """
    Plots the historical series and multiple forecasts from different models.

    Parameters:
    original_series (pd.Series): Original time series.
    forecast_list (list of pd.Series): List of forecasted time series.
    model_list (list of str): List of model names corresponding to the forecasts.
    """
    plt.plot(original_series, label='Historical Series', linestyle='-')
    colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
    for i, (forecast, model) in enumerate(zip(forecast_list, model_list)):
        plt.plot(forecast, label=model, linestyle='--', color=colors[i % len(colors)])
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.title('Historical Series with Forecasts')
    plt.legend()
    plt.show()

def cross_correlation(y, x, max_lags=24, title='Cross-Correlation'):
    """
    Calculates and plots the cross-correlation between two time series with specified lags.

    Parameters:
    y (pd.Series): Dependent time series.
    x (pd.Series): Independent time series.
    max_lags (int): Maximum number of lags to consider for cross-correlation.
    """
    correlations = []
    lags = range(-max_lags, max_lags + 1)
    for lag in lags:
        corr = y.corr(x.shift(lag))
        correlations.append(corr)
    plt.figure(figsize=(10, 5))
    plt.stem(lags, correlations)
    plt.xlabel('Lag')
    plt.title(title)
    conf_interval = 1.96 / np.sqrt(len(y))
    plt.axhline(-conf_interval, color='k', ls='--')
    plt.axhline(conf_interval, color='k', ls='--')
    plt.show()

def compare_statistics(model_list, model_list_names):
    """
    Compares statistical metrics (BIC, AIC, RMSE) of different models.

    Parameters:
    model_list (list): A list of fitted model objects.
    model_list_names (list): A list of names corresponding to the models.
    """
    for model, name in zip(model_list, model_list_names):
        rmse = round(np.sqrt(np.mean(model.resid**2)))
        bic = round(model.bic)
        aic = round(model.aic)
        print(f'BIC = {bic} -- AIC = {aic} -- RMSE = {rmse} - {name}')

def first_order_look(y):
    """
    Calculates and plots the first-order difference of a time series.

    Parameters:
    y (pd.Series): Time series.
    """
    first_order_diff = y.diff().dropna()
    first_order_diff.plot()
    plt.show()
    print(stationarity_tests(first_order_diff))