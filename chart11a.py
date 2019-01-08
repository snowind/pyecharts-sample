from pyecharts import Bar,Line,Overlap, Page
import pandas as pd
import random
import numpy as np 

page = Page()



xline = pd.date_range(start='12/1/2018', periods=10)
#v1 = random.sample(range(100), 10)
#v2 = random.sample(range(100), 10)
v1 = [10,20,30,40,50,60,40,80,30,20]
v2 = [38,28,35,58,65,70,20,40,90,10]

bar = Bar('Line - Bar示例')
bar.add('bar',xline,v1)
line = Line()
line.add('line',xline,v2)

overlop = Overlap()
overlop.add(bar)
overlop.add(line)

page.add(overlop)
page.render('./picture11a.html')
