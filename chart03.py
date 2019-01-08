from pyecharts import Bar

attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1 = [5,20,36,10,75,90]
v2 = [10,25,8,60,20,80]
bar = Bar('柱状信息堆叠图')
bar.add('商家A',attr,v1,is_stack = True)  #is_stack = True才表示堆叠在一起
bar.add('商家B',attr,v2,is_stack = True)
bar.render('./picture3.html')  
