import pyecharts
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.use_theme('dark')                                  #暗色背景色
bar.add("服装",                                        #注解==label
        ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"], #横坐标
        [5, 20, 36, 10, 75, 90])                       #纵坐标
bar.render('./picture1.html')                          #文件存储路径（默认保存当前文件路径）
