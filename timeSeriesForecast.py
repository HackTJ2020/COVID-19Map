def predict_Graphs(state):    
    import warnings
    import itertools
    import numpy as np
    from pylab import rcParams
    import matplotlib.pyplot as plt
    warnings.filterwarnings("ignore")
    plt.style.use('fivethirtyeight')
    import pandas as pd
    import statsmodels.api as sm
    import matplotlib
    matplotlib.rcParams['axes.labelsize'] = 14
    matplotlib.rcParams['xtick.labelsize'] = 12
    matplotlib.rcParams['ytick.labelsize'] = 12
    matplotlib.rcParams['text.color'] = 'k'

    df = pd.read_csv("csvFiles/"+state+"_covrec.csv")
    cases = df
    cases["Date"] = pd.to_datetime(cases["Date"])
    cases = cases.set_index("Date")
    #print(cases.index)
    y=cases["New Cases"].resample('SM').mean()
    #y.plot(figsize=(15,6))
    #plt.show()
    rcParams['figure.figsize'] = 18, 8
    print(y)
    decomposition = sm.tsa.seasonal_decompose(y, model='additive', period=5)
    decomposition.plot()
    plt.savefig("Graphs/"+state+"decompose.jpg")
    plt.close()

    p = d = q = range(0, 2)
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = [(x[0], x[1], x[2], 2) for x in list(itertools.product(p, d, q))]
    print('Examples of parameter combinations for Seasonal ARIMA...')
    print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
    print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
    print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
    print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))
    #finds best parameters that yields best performance:
    warnings.filterwarnings("ignore")
    res = 10000
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(y,
                                                order=param,
                                                seasonal_order=param_seasonal, 
                                                enforce_stationarity=False, 
                                                enforce_invertibility=False)
                results = mod.fit(disp=0)
                print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                if results.aic<res:
                    res = results.aic
                    print(res)
                    par = param
                    pars = param_seasonal

            except:
                continue
    mod = sm.tsa.statespace.SARIMAX(y,
                                    order=par,
                                    seasonal_order=pars,
                                    enforce_stationarity=False,
                                    enforce_invertibility=False)
    results = mod.fit(disp=0)
    print(results.summary().tables[1])
    results.plot_diagnostics(figsize=(16, 8))
    plt.savefig("Graphs/"+state+"graphs.jpg")
    plt.close()

    pred = results.get_prediction(start=pd.to_datetime('2020-07-15'), dynamic=False)
    pred_ci = pred.conf_int()
    ax = y['2020':].plot(label='observed')
    pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', 
    alpha=.7, figsize=(14, 7))

    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.2)

    ax.set_xlabel('Date')
    ax.set_ylabel('New Cases')
    plt.legend()

    plt.savefig("Graphs/"+state+"prediction.jpg")
    plt.close()

    y_forecasted = pred.predicted_mean
    y_truth = y['2020-07-15':]
    mse = ((y_forecasted - y_truth) ** 2).mean()
    print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))
    print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))
    pred_uc = results.get_forecast(steps=10)
    pred_ci = pred_uc.conf_int()
    ax = y.plot(label='observed', figsize=(14, 7))
    pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.25)
    ax.set_xlabel('Date')
    ax.set_ylabel('New Cases')
    plt.legend()
    plt.savefig("Graphs/"+state+"Future.jpg")
    plt.close()

predict_Graphs("VA")