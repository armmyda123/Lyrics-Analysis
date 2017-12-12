import plotly.plotly as py
import plotly.graph_objs as go
import plotly

labels = ['Non-Popular Song', 'Popular Song']
values = [232, 232]
trace = go.Pie(labels=labels, values=values)
plotly.offline.plot([trace])
