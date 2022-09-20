# -*- encoding: utf-8 -*-
'''
@Description: Plot MV of BTC
@Author: Yang Boyu
@Email: bradleyboyuyang@gmail.com
@File: plot_btc.py
@Date: 2022/09/20 17:47:06
@version: 1.0
'''

# 可通过 pip install pyecharts 指令下载相应库
import pyecharts.options as opts
import pandas as pd
from pyecharts.charts import Line

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 每一行的宽度（避免换行）


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


    