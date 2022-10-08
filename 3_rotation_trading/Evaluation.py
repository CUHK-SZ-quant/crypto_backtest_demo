import pandas as pd
import numpy as np

def evaluate_investment(df, title, time='date') -> pd.DataFrame:
    """
    @description : 计算策略评价指标
    @param df    : 包含时间与净值曲线的dataframe
    @param title : df中净值曲线的列名
    @param date  : df中时间列的列名
    @returns     : 策略评价的结果
    """
    temp = df.copy()
    # 保存回测结果
    results = pd.DataFrame()

    # 计算累积净值
    results.loc[0, 'cumulative_return'] = round(temp[title].iloc[-1], 2)

    # 计算年化收益
    annual_return = (temp[title].iloc[-1]) ** ('1 days 00:00:00' / (temp[time].iloc[-1] - temp[time].iloc[0]) * 365) - 1
    results.loc[0, 'annual_return'] = str(round(annual_return * 100, 2)) + '%'

    # 计算最大回撤
    temp['max2here'] = temp[title].expanding().max()
    temp['dd2here'] = temp[title] / temp['max2here'] - 1

    # 计算最大回撤结束日期
    end_date, max_draw_down = tuple(temp.sort_values(by=['dd2here']).iloc[0][[time, 'dd2here']])

    # 计算最大回撤开始日期
    start_date = temp[temp[time] <= end_date].sort_values(by=title, ascending=False).iloc[0][time]

    # 删除无关变量
    temp.drop(['max2here', 'dd2here'], axis=1, inplace=True)
    results.loc[0, 'max_drawdown'] = format(max_draw_down, '.2%')
    results.loc[0, 'drawdown_begin'] = str(start_date)
    results.loc[0, 'drawdown_end'] = str(end_date)

    # 计算收益回撤比
    results.loc[0, 'return/drawdown'] = round(annual_return / abs(max_draw_down), 2)

    # 计算年化夏普
    results.loc[0, 'sharpe_ratio'] = temp[title].pct_change().mean()/temp[title].pct_change().std()*np.sqrt(252)

    results.index = ['Performance']
    return results.T