from pyecharts import Line

attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1 = [5,20,36,10,75,90]
v2 = [10,25,8,60,20,80]
line = Line('折线面积示例图')
line.add('商家A',attr,v1,is_fill = True,
    line_opacity = 0.2,      #线条不透明度
    area_opacity = 0.4,
    symbol = None)  
line.add('商家B',attr,v2,is_fill = True,
    line_color = '#000',     #黑色
    area_opacity = 0.3,      #填充不透明度
    is_smooth = True)
line.render('./picture6.html') 
