import plotly
import plotly.plotly as py
from plotly.graph_objs import *
def main():
    """Plot the graph by non-popular song compare popular song
    lis_x is word frequency of non-popular song
    lis_y is word frequency of popular song
    lis_y is the most word in non-popular song"""
    lis_x = [104, 69, 77, 74, 76, 91, 51, 47, 35, 58, 23, 31, \
             25, 37, 17, 17, 16, 16, 16, 5]
    lis_x1 = [129, 119, 106, 100, 96, 96, 80, 78, 63, 53, 44\
              , 30, 33, 32, 23, 22, 21, 21, 21, 12]
    lis_y = ['Love', 'Yeah', 'Make', 'Come', 'Want', 'Feel', 'Tell', \
             'Look', 'Give', 'Talk', 'Play', 'Town', 'Stay', 'Before', \
             'Sing', 'Wish', 'Say', 'Care', 'Year', 'Pass']
    plotly.offline.plot(({
        "data": [Scatter(x=lis_y, y=lis_x, name='Non-Popular Song', line = dict(color = '#FF5028'), opacity=5.0), Scatter(x=lis_y, y=lis_x1, name='Popular Song', line=dict(color="#0000FF"))],
        "layout": Layout(title="Non-Popular Song Compare Popular Song")
    }))
main()
