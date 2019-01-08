from pyecharts import Line,Bar,Overlap, Page 

page = Page()

attr = ["{}月".format(i) for i in range(1, 13)]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
line1 = Line("多 Y 轴叠加")
line1.add("SYS1", attr, v1, is_stack=True,  area_opacity=0.5)  
line1.add("SYS2", attr, v2, is_stack=True,  area_opacity=0.5)  
line2 = Line()
line2.add("Usage", attr, v3, yaxis_formatter=" %")

chart = Overlap()
chart.add(line1)
chart.add(line2, yaxis_index=1, is_add_yaxis=True)

page.add(chart)


prod = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1 = [5,20,36,10,75,90]
v2 = [10,25,8,60,20,80]
line3 = Line('折线示例图')
line3.add('商家A',prod,v1,is_stack=True,area_opacity=0.5, mark_point = ['average'])    
line3.add('商家B',prod,v2,is_stack=True,area_opacity=0.5, mark_line = ['max','average'])

page.add(line3)
page.render('./picture5a.html')
