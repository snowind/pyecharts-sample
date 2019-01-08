from pyecharts import Bar,Line,Overlap

xline = ['A','B','C','D','E','F']
v1 = [10,20,30,40,50,60]
v2 = [38,28,35,58,65,70]

bar = Bar('Line - Bar示例')
bar.add('bar',xline,v1)
line = Line()
line.add('line',xline,v2)

overlop = Overlap()
overlop.add(bar)
overlop.add(line)
overlop.render('./picture11.html')
