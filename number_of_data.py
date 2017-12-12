import plotly.plotly as py
import plotly.graph_objs as go
import plotly
""" This code makeing Pie Graph respresent all data of Popular Song and \
Non-Popular Song """
labels = ['Non-Popular Song', 'Popular Song']
values = [232, 232]
trace = go.Pie(labels=labels, values=values)
plotly.offline.plot([trace])
