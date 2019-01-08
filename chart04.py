from pyecharts import Bar

attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1 = [5,20,36,10,75,90]
v2 = [10,25,8,60,20,80]
bar = Bar('标记线和标记示例')
bar.add('商家A',attr,v1,mark_line = ['min','max'])     #标记点：商家A的平均值
bar.add('商家B',attr,v2,mark_line = ['min','max'])    #标记线：商家B最小/最大值
bar.render('./picture4.html')
