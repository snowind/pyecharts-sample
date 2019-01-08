from pyecharts import Line,EffectScatter,Overlap
attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1 = [5,20,36,10,10,90]
line = Line('线性_闪烁图示例')
line.add('',attr,v1,is_random = True)

es = EffectScatter()
es.add('',attr,v1,effect_scale=8)   #闪烁
overlop = Overlap()
overlop.add(line)                   #必须先添加line,在添加es
overlop.add(es)
overlop.render('./picture12.html')
