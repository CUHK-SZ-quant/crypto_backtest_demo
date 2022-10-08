import pandas as pd
import numpy as np

def evaluate_investment(source_data, title, time='date'):
    temp = source_data.copy()
    # keep the backtesting result
    results = pd.DataFrame()

    # calculate cumulative net worth
    results.loc[0, 'cumulative_return'] = round(temp[title].iloc[-1], 2)

    # calculate annual return
    annual_return = (temp[title].iloc[-1]) ** ('1 days 00:00:00' / (temp[time].iloc[-1] - temp[time].iloc[0]) * 365) - 1
    results.loc[0, 'annual_return'] = str(round(annual_return * 100, 2)) + '%'

    # calculate maximum drawdown
    # maximum value curve till today
    temp['max2here'] = temp[title].expanding().max()
    # drawdown
    temp['dd2here'] = temp[title] / temp['max2here'] - 1
    # calculate maximum drawdown and its recover period
    end_date, max_draw_down = tuple(temp.sort_values(by=['dd2here']).iloc[0][[time, 'dd2here']])
    # begin_period
    start_date = temp[temp[time] <= end_date].sort_values(by=title, ascending=False).iloc[0][time]
    # delete irrelevant variables
    temp.drop(['max2here', 'dd2here'], axis=1, inplace=True)
    results.loc[0, 'max_drawdown'] = format(max_draw_down, '.2%')
    results.loc[0, 'drawdown_begin'] = str(start_date)
    results.loc[0, 'drawdown_end'] = str(end_date)
    # annual_return divided by maximum drawdown
    results.loc[0, 'return/drawdown'] = round(annual_return / abs(max_draw_down), 2)
    # sharpe ratio
    results.loc[0, 'sharpe_ratio'] = temp[title].pct_change().mean()/temp[title].pct_change().std()*np.sqrt(252)

    results.index = ['Performance']
    return results.T