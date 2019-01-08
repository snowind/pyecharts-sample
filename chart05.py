from pyecharts import Line

attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1 = [5,20,36,10,75,90]
v2 = [10,25,8,60,20,80]
line = Line('折线示例图')
line.add('商家A',attr,v1,is_stack=True,area_opacity=0.5, mark_point = ['average'])    
line.add('商家B',attr,v2,is_stack=True,area_opacity=0.5, mark_line = ['max','average'])
line.render('./picture5.html')
