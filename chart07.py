from pyecharts import Pie

attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1 = [5,20,36,10,75,90]
pie = Pie('饼图-环形图示例',title_pos = 'center')
pie.add(
        '',attr,v1,                 #''：图例名（不使用图例）
        radius = [40,75],           #环形内外圆的半径
        is_label_show = True,       #是否显示标签
        label_text_color = None,    #标签颜色
        legend_orient = 'vertical', #图例垂直
        legend_pos = 'left'
        )
pie.render('./picture7.html') 
