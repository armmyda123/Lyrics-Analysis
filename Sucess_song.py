import plotly
import plotly.plotly as py
from plotly.graph_objs import *
def main():
    """Plot the graph based on the number of words used in most successful songs"""
    """list_x is count word"""
    """list_y is top 20 in most word"""
    lis_x = [108, 107, 98, 73, 69, 49, 46, 45, 42, 39, 34, 27, 25, 24, 20, 18, 11, 11, 6, 6]
    lis_y = ['Time', 'Baby', 'Take', 'Keep', 'Good', 'Life', 'Little', 'Mind', 'Get', 'Eye', 'Fall',\
             'Fire', 'Dream', 'Dance', 'Rock', 'Hell', 'Music', 'Lone', 'Thang', 'Die']
    plotly.offline.plot(({
        "data": [Pie(labels=lis_y, values=lis_x)],
        "layout": Layout(title="Popular Song")
    }))
main()
