from pyecharts import Bar
bar = Bar('基本柱状图','副标题')
bar.add('服装',
        ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子'],
        [5,20,36,10,75,90],
        is_more_utils = True,      #设置最右侧工具栏
        yaxis_min = 0,
        yaxis_max = 200
        )
#bar.show_config()               #调试输出pyecharts的js配置信息
bar.render('./picture2.html')
