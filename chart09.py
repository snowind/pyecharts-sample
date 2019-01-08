from pyecharts import WordCloud
name = [
        'Though','the answer','this question',
        'may at first','seem to border','on the',
        'absurd','reflection','will show','that there',
        'is a','good deal','more in','it than meets','the eye'
        ]
value = [10000,6189,4556,2356,2233,
         1895,1456,1255,981,875,
         542,462,361,265,125]
worldcloud = WordCloud(width = 1300,height = 620)
worldcloud.add('',name,value,word_size_range = [20,100])
worldcloud.render('./picture9.html')
