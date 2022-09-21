'''
简单定投收益回测
额外说明详见README.md

'''
import pandas as pd
import logging 

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180)

static_amount = 100
start_date = '2006-12-04'
end_date = '2022-12-31'

df = pd.read_csv('./data/BTCUSD_1D.csv')

df = df[['candle_begin_time', 'close']] 
df = df[(df['candle_begin_time'] >= start_date) & (df['candle_begin_time'] <= end_date)]
df.reset_index(drop=True, inplace=True)

# 计算累计投入资金
df['每次投入资金'] = 100  
df['累计投入资金'] = df['每次投入资金'].cumsum()  

# 计算累计买币数量
c_rate = 0.002  # 手续费加滑点，远高于市场水平
df['每次买币数量'] = df['每次投入资金'] * (1-c_rate) / df['close'] # 扣除手续费，并不精确
df['累计买币数量'] = df['每次买币数量'].cumsum() 

# 计算币的市值
df['平均持有成本'] = df['累计投入资金'] / df['累计买币数量']
df['币市值'] = df['累计买币数量'] * df['close']

print(df)

df['资金曲线'] = df['币市值'] - df['累计投入资金']



# 输出结果
df.to_csv('result.csv', index=False)
# 13到15年，每日定投100，赚了20000块