"""
>>> 最简单的量化策略：定投
>>> 牛市定投，少赚一点，因为这是不微笑曲线，本来平摊成本现在平摊了收益；但熊市定投，会少亏很多。长期来看，定投有很强的盈利水平

"""
import numpy as np
import pandas as pd
import os
pd.set_option('expand_frame_repr', True) # pycharm设置为False可以产生滑条，但vscode不能产生滑条所以会堆叠。因此vscode应该设置为True
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 每一行的宽度（避免换行）
pd.set_option('display.max_rows', 100) # 显示的最大行数（避免只显示部分行数据）
pd.set_option('display.max_columns', 100) # 显示的最大列数（避免列显示不全）
# pd.set_option('display.float_format', lambda x: '%.3f' % x)    # 取消Pandas 科学计数法显示 + 可调节位数

DATA_PATH = r'E:\BradleyStrats\BasicCrypto\src\1_static_trade\data'
SAVE_PATH = r'E:\BradleyStrats\BasicCrypto\src\1_static_trade\results'

df = pd.read_csv(DATA_PATH + '\\BTCUSD_1D.csv', skiprows=1)
df = df[['candle_begin_time', 'close']] 

# ===选取时间段
# 牛市回测2017-01-01到2017-12-31
# 熊市回测2018-01-01到2018-12-31
# 长期回测就2006至今，稳赚不赔
# 最坏情况：牛市顶点开始定投，2013-12-04至今
# 测试一个完整的微笑曲线，EOSUSD从2018-01-13到2018-04-26，16美金价格牛市顶点再涨回去的过程
# BTC完整的微笑曲线，BTCUSD_1D，2017-12-17到2018-05-05，比特币腰斩，定投不亏
# 观测定投微笑曲线如何降低平均持币成本：BTCUSD，2013-12-04到2015-12-31，牛市顶点定投，持币成本最后还会低于收盘价
# 两个参数：定投的资金量和定投频率。资金量可以直接该参数，更换频率需要更换数据集，代码上不好改
df = df[df['candle_begin_time'] >= '2013-12-04']  # 定投开始时间
df = df[df['candle_begin_time'] <= '2015-12-31']  # 定投结束时间

# ===计算累计投入资金
df['每次投入资金'] = 100  # 每个周期投入100元买币
df['累计投入资金'] = df['每次投入资金'].cumsum()  # 至今累计投入的资金，cumulative_sum

# ===计算累计买币数量
c_rate = 0.002  # 手续费，回测一定要精确
df['每次买币数量'] = df['每次投入资金'] / df['close']*(1-c_rate) #每个周期买入币的数量，扣除手续费（此处手续费计算有近似）
df['累计买币数量'] = df['每次买币数量'].cumsum()  # 累计买入币的数量

# ===计算币的市值
df['平均持有成本'] = df['累计投入资金'] / df['累计买币数量']
df['币市值'] = df['累计买币数量'] * df['close']

# ===输出数据
print(df.tail(50))
df.to_csv(os.path.join(SAVE_PATH, '定投结果.csv'), index=False)
# 13到15年，每日定投100，赚了20000块