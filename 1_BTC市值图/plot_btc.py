# -*- encoding: utf-8 -*-
'''
@Description: 
@Date: 2022/09/20 17:42:46
@Author: Yang Boyu
@version: 1.0
'''

# 可通过 pip install pyecharts 指令下载相应库
import pyecharts.options as opts
import pandas as pd
from pyecharts.charts import Line
import os

pd.set_option('expand_frame_repr', True) # pycharm设置为False可以产生滑条，但vscode不能产生滑条所以会堆叠。因此vscode应该设置为True
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 每一行的宽度（避免换行）
pd.set_option('display.max_rows', 100) # 显示的最大行数（避免只显示部分行数据）
pd.set_option('display.max_columns', 100) # 显示的最大列数（避免列显示不全）
# pd.set_option('display.float_format', lambda x: '%.3f' % x)    # 取消Pandas 科学计数法显示 + 可调节位数


df = pd.read_csv("btc_mv.csv", encoding='gbk')
print(df.head(20))
x_data = df['交易日期']
y_data = df['总市值（亿美元）']

# pyecharts画折线图
(
    Line()
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .render("btc_mv_plot.html")
)



    