import plotly
import plotly.plotly as py
from plotly.graph_objs import *
def main():
    lis_x1 = [103, 33, 80, 43, 46, 50, 32, 41, 30, 42, 41, 18, 29, 14, 5, 23, 3, 13, 2, 10]
    lis_x = [108, 107, 98, 73, 69, 49, 46, 45, 42, 39, 34, 27, 25, 24, 20, 18, 11, 11, 6, 6]
    lis_y1 = ['Time', 'Baby', 'Take', 'Keep', 'Good', 'Life', 'Little', 'Mind', 'Get', 'Eye', 'Fall', 'Fire', 'Dream', 'Dance', 'Rock', 'Hell', 'Music', 'Lone', 'Thang', 'Die']
    plotly.offline.plot(({
        "data": [Scatter(x=lis_y1, y=lis_x, name='Popular Song', line=dict(color="#0000FF")), Scatter(x=lis_y1, y=lis_x1, name='Non-Popular Song', line = dict(color = '#FF5028'))],
        "layout": Layout(title="Popular Song Compare Non-Popular Song")
    }))
main()
