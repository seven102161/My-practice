import pandas as pd
import json
# from matplotlib import pyplot as plt
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts.charts import HeatMap
from pyecharts.faker import Faker


df = pd.read_csv('an.business.csv', sep=',')

# df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 19 entries, 0 to 18
Data columns (total 9 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   building            19 non-null     object 
 1   address             19 non-null     object 
 2   area                19 non-null     object 
 3   total_floors        19 non-null     object 
 4   size                19 non-null     float64
 5   size_range          19 non-null     object 
 6   daily_price         19 non-null     float64
 7   monthly_price       19 non-null     float64
 8   monthly_price_size  19 non-null     float64
dtypes: float64(4), object(5)
memory usage: 1.5+ KB
'''

# print('-------------------------------------\n')
mean_area = (df.loc[:, ['area', 'daily_price', 'monthly_price_size']].groupby('area').mean())
mean_area = mean_area.reset_index()
# print('按楼层区域划分: 【日单价（元/平方） 月单价（元/平方）】\n', mean_area)
# print('-------------------------------------\n')

'''
按楼层区域划分【日单价（元/平方） 月单价（元/平方）】: 
   area  daily_price  monthly_price_size
0   中区     1.864286           55.910718
1   高区     1.790000           53.691892
'''

mean_floors = (df.loc[:, ['total_floors', 'daily_price', 'monthly_price_size']].groupby('total_floors').mean())
mean_floors = mean_floors.reset_index()
# print('按最高楼层划分: 【日单价（元/平方） 月单价（元/平方）】\n', mean_floors)
item_floor = dict()
top_floor = list(mean_floors['total_floors'])
# print(top_floor)
price_top_floor = [round(i, 2) for i in mean_floors['daily_price']]
# print(price_top_floor)
item_floor['categories'] = top_floor
item_floor['data'] = price_top_floor
print(item_floor)
with open('an_business_bar.json', 'w', encoding='utf-8') as fp:
    json.dump(item_floor, fp)
print('写入成功！')

# print('-------------------------------------\n')

'''
按最高楼层划分: 【日单价（元/平方） 月单价（元/平方）】
   total_floors  daily_price  monthly_price_size
0          20层     1.860000           55.774123
1          24层     2.050000           61.500000
2          25层     1.872222           56.148766
3          26层     1.400000           42.000000
4          31层     1.700000           51.000000
'''

mean_size = (df.loc[:, ['size_range', 'daily_price', 'monthly_price_size']].groupby('size_range').mean())
mean_size = mean_size.reset_index()
# print('按楼出租面积划分:【日单价（元/平方） 月单价（元/平方）】 \n', mean_size)
# print('-------------------------------------\n')

'''
按楼出租面积划分: 【日单价（元/平方） 月单价（元/平方）】
      size_range  daily_price  monthly_price_size
0      (0, 100]     1.400000           42.000000
1    (100, 500]     1.866667           55.983076
2  (1000, 2000]     1.940000           58.194721
3   (500, 1000]     1.787500           53.597054
'''


# p1 = plt.figure(figsize=(12, 6))
#
# p1.add_subplot(1, 2, 1)
# plt.title('Distribution of Size')
# size = df['size']
# group = [i for i in range(0, 2000, 200)]
# plt.hist(size, group)
# plt.xticks(group)
#
# p1.add_subplot(1, 2, 2)
# plt.title('Monthly price per size')
# x = df['size_range']
# y = df['monthly_price_size']
# plt.bar(x, y, color='sandybrown')
# plt.xticks(x)

# plt.savefig('an_business.png')
# plt.show()

# ----------------------------------------------------------------------
# bar = Bar()
# bar.add_xaxis(list(mean_floors['total_floors']))
# bar.add_yaxis("楼层单价", list(mean_floors['daily_price']))
# # bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="青岛国际创新园"))
# bar.render()

# bar = (
#     Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
#     .add_xaxis(top_floor)
#     .add_yaxis("楼层总高&单价", price_top_floor)
#     .set_global_opts(title_opts=opts.TitleOpts(title="青岛国际创新园"))
# )
# bar.render()
# make_snapshot(snapshot, bar.render(), "bar.png")


# -----------------------------------------------------------------
# line
# x_data = list(mean_floors['total_floors'])
# y_data = list(mean_floors['daily_price'])

# (
#     Line()
#     .set_global_opts(
#         tooltip_opts=opts.TooltipOpts(is_show=False),
#         xaxis_opts=opts.AxisOpts(type_="category"),
#         yaxis_opts=opts.AxisOpts(
#             type_="value",
#             axistick_opts=opts.AxisTickOpts(is_show=True),
#             splitline_opts=opts.SplitLineOpts(is_show=True),
#         ),
#     )
#     .add_xaxis(xaxis_data=x_data)
#     .add_yaxis(
#         series_name="",
#         y_axis=y_data,
#         symbol="emptyCircle",
#         is_symbol_show=True,
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#     .render("basic_line_chart.html")
# )

# heat map --------------------------------------------------
# piv_price = pd.pivot_table(df, columns='total_floors', index='size_range', values='monthly_price_size', aggfunc='mean')
# values = piv_price.values
# x = piv_price.columns
#
# y = piv_price.index
#
# value_list = []
# for i in values:
#     for j in i:
#         value_list.append(j)
# print(len(value_list))
# data = [[i, j] for i in range(len(x)) for j in range(len(y))]
# print(len(data))
# for i in range(len(data)):
#     data[i].append(value_list[i])
# # print(data)
#
# (
#     HeatMap()
#     .add_xaxis(xaxis_data=list(x))
#     .add_yaxis(
#         series_name="Punch Card",
#         yaxis_data=list(y),
#         value=data,
#         label_opts=opts.LabelOpts(
#             is_show=True, color="#fff", position="bottom", horizontal_align="50%"
#         ),
#     )
#     .set_series_opts()
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="青岛国际创新园"),
#         legend_opts=opts.LegendOpts(is_show=False),
#         xaxis_opts=opts.AxisOpts(
#             type_="category",
#             splitarea_opts=opts.SplitAreaOpts(
#                 is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
#             ),
#         ),
#         yaxis_opts=opts.AxisOpts(
#             type_="category",
#             splitarea_opts=opts.SplitAreaOpts(
#                 is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
#             ),
#         ),
#         visualmap_opts=opts.VisualMapOpts(
#             min_=0, max_=10, is_calculable=True, orient="horizontal", pos_left="center"
#         ),
#     )
#     .render("heatmap_on_cartesian.html")
# )
