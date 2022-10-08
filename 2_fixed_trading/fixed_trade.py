'''
@Description: 双币轮动_v1收益回测，不考虑空仓
@Author: Yang Boyu
@Email: bradleyboyuyang@gmail.com
'''

import pandas as pd
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180)
pd.set_option('display.float_format', lambda x: '%.3f' % x)  

# 参数设置
static_amount = 100
start_date = '2013-12-04'
end_date = '2015-12-31'

df = pd.read_csv('./data/BTCUSD_1D.csv')

df = df[['candle_begin_time', 'close']]
df = df[(df['candle_begin_time'] >= start_date) & (df['candle_begin_time'] <= end_date)]
df['candle_begin_time'] = pd.to_datetime(df['candle_begin_time'])
df.set_index('candle_begin_time', inplace=True)

# 计算累计投入资金
df['每次投入资金'] = 100
df['累计投入资金'] = df['每次投入资金'].cumsum()

# 计算累计买币数量
c_rate = 0.002  # 手续费加滑点，远高于市场水平
df['每次买币数量'] = df['每次投入资金'] * (1-c_rate) / df['close']  # 扣除手续费，并不精确
df['累计买币数量'] = df['每次买币数量'].cumsum()

# 计算币的市值
df['平均持有成本'] = df['累计投入资金'] / df['累计买币数量']
df['币市值'] = df['累计买币数量'] * df['close']
df['盈亏PnL'] = df['币市值'] - df['累计投入资金']
df['总收益率'] = (df['币市值'] / df['累计投入资金']-1).apply(lambda x: f'{round(x*100, 3)}%')

total_inv = round(df['累计投入资金'].iloc[-1], 2)
total_asset = round(df['币市值'].iloc[-1], 2)
ratio = round(total_asset / total_inv, 2)

print(df)

print(f"定投总投入：{total_inv}， 总资产：{total_asset}，资产投入比：{ratio}")

# 输出结果
df.to_csv('result.csv', index=True)