from pyecharts import Scatter
v1 = [5,20,35,50,65,80]
v2 = [10,20,30,40,50,60]
scatter = Scatter('散点-气泡示例图')
scatter.add('A',v1,v2)
scatter.add('B',v1[::-1],v2,                #v1[::-1]代表切片倒序
            is_visualmap = True,            #显示滑动条
            symbol_size = 30,               #显示图内标点大小
            vasual_range_size = [20,80])    #显示滑动范围
scatter.render('./picture8.html')   
