'''
@Description: 超参数设置
@Author: Yang Boyu
@Email: bradleyboyuyang@gmail.com
'''

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180)

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 轮动双币名称
symbol1 = 'BTCUSD'
symbol2 = 'ETHUSD'

# 数据频率
freq = '1d'

# 交易参数
trade_rate = 2.5 / 1000  # 千分之2.5的交易费用远高于市场平均水平
momentum_days = 20  # 计算多少天的涨跌幅