
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
def main():
    lis_x = [2547, 2548, 2549, 2550, 2547, 2548, 2549, 2550, 2547, 2548, 2549, 2550]
    plotly.offline.plot(({
        "data": [Scatter(x=lis_x, y=[10, 20])],
        "layout": Layout(title="Sample Test")
    }))
main()
