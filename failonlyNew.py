import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from plotly.graph_objs import *
def main():
    labels = ['Love', 'Yeah', 'Make', 'Come', 'Want', 'Feel', 'Tell', \
             'Look', 'Give', 'Talk', 'Play', 'Town', 'Stay', 'Before', \
             'Sing', 'Wish', 'Say', 'Care', 'Year', 'Pass']
    values = [104, 69, 77, 74, 76, 91, 51, 47, 35, 58, 23, 31, \
             25, 37, 17, 17, 16, 16, 16, 5]
    plotly.offline.plot(({
        "data": [Pie(labels=labels, values=values)],
        "layout": Layout(title="Non-Popular Song")
    }))
main()
