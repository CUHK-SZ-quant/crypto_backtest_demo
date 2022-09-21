'''
BTC市值走势绘制

'''
import pandas as pd
from pyecharts.charts import Line
import pyecharts.options as opts

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) 

df = pd.read_csv("btc_mv.csv")
print(df.head(20))

# 市值的单位是亿美元
x_data = df['datetime'].tolist()
y_data = df['mv'].round(1).tolist()

# 绘制折线图
line = Line()
line.add_xaxis(xaxis_data=x_data)
line.add_yaxis(
    series_name="BTC/USDT",       
    y_axis=y_data,  
    symbol="emptyCircle",
    is_symbol_show=True,
    areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color='#00FFFF'),  # 设置图形透明度与填充颜色
    label_opts=opts.LabelOpts(is_show=False),   # 标签配置项
    markpoint_opts=opts.MarkPointOpts(         # 标记点配置项
        data=[
                opts.MarkPointItem(type_="max", name="max"),
                opts.MarkPointItem(type_="average", name="avg")
        ]
    ),
    markline_opts=opts.MarkLineOpts(           # 标记线配置项
        data=[opts.MarkLineItem(type_="average", name="avg")])
)
line.set_global_opts(
    title_opts=opts.TitleOpts(title='Bitcoin Market Value (2013-2021)')
)
line.render("btc_mv_plot.html") 
