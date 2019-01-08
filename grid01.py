import random
from pyecharts import HeatMap, Bar, Grid, Page

page = Page()
x_axis = [
    "12a", "1a", "2a", "3a", "4a", "5a", "6a",
    "7a", "8a", "9a", "10a", "11a", "12p", "1p",
    "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
    "10p", "11p",
]
y_axis = [
    "Saturday",
    "Friday",
    "Thursday",
    "Wednesday",
    "Tuesday",
    "Monday",
    "Sunday",
]
data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
heatmap = HeatMap("热力图示例")
heatmap.add(
    "热力图直角坐标系",
    x_axis,
    y_axis,
    data,
    is_visualmap=True,
    visual_top="45%",
    visual_text_color="#000",
    visual_orient="horizontal",
)
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", title_top="52%")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True, legend_top="50%")

grid = Grid(height=700)
grid.add(heatmap, grid_bottom="60%")
grid.add(bar, grid_top="60%")

page.add(grid)
page.render('./grid01.html')
