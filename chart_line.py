import pandas as pd
from pyecharts import Bar, Line, Pie
from pyecharts import Page, Style

x = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
y1 = [5, 20, 36, 10, 75, 90]
y2 = [10, 25, 8, 60, 20, 80]

page = Page()
style = Style()
bar_style = style.add(
    mark_point=["max", "min"],
    mark_line=["average"],
    is_label_show=True,
    is_more_utils=True)
bar = Bar()
bar.add('', x, y1, **bar_style)
bar.add('', x, y2, **bar_style)
page.add(bar)

line = Line()
line_style = style.add(
    mark_point=["max", "min"],
    mark_line=["average"],
    is_label_show=False,
    is_more_utils=False,
    is_stack=True,
    is_fill=True,
    area_opacity=0.5    
    )
line.add('', x, y1, **line_style)
line.add('', x, y2, **line_style)
page.add(line)

pie = Pie("饼图-玫瑰图示例")
pie_style=style.add(
    is_random=True,
    radius=[30, 75],
    rosetype="area",
    is_legend_show=True,
    is_label_show=True)
pie.add(
    "商品A",
    x,
    y1,
    center=[25, 50],
    **pie_style)
pie.add(
    "商品B",
    x,
    y2,
    center=[75, 50],
    **pie_style)
page.add(pie)
page.render('./picture_line.html')
