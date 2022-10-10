'''
@Description: 策略对比画图
@Author: Yang Boyu
@Email: bradleyboyuyang@gmail.com
'''

from Config import *

res1 = pd.read_csv("./results/rotation_v1.csv", encoding='gbk', parse_dates=['candle_end_time'])
res2 = pd.read_csv("./results/rotation_v2.csv", encoding='gbk', parse_dates=['candle_end_time'])

res1 = res1[['candle_end_time', 'coin1_net', 'coin2_net', 'strategy_net']]
res2 = res2[['candle_end_time', 'strategy_net']]

res = pd.merge(res1, res2, suffixes=("_v1", "_v2"), on='candle_end_time').set_index('candle_end_time')
res.rename(columns={'coin1_net': f'{symbol1}', 'coin2_net': f'{symbol2}', 'strategy_net_v1': 'rotation_v1', 'strategy_net_v2': 'rotation_v2'}, inplace=True)

print(res)

fig, ax = plt.subplots(1,1,figsize=(10,6))
plt.style.use('seaborn-dark')
res.plot(ax=ax, kind='line', grid=True, color=['magenta', 'g', 'b', 'r'], figsize=(12, 8), legend=True)

plt.savefig("./images/comparison.png", dpi=400)

plt.show()