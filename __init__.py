# __init__.py
import pyecharts as pe
from charts import add, add_df


for __name in dir(pe):
    if __name[0].isupper():
        locals()[__name] = type(__name, (getattr(pe, __name), ), {'add': add, 'add_df': add_df})