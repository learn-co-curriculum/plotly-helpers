import plotly
from plotly.offline import iplot

def trace(data, markers = True):
    x_values = list(map(lambda point: point['x'],data))
    y_values = list(map(lambda point: point['y'],data))
    return {'x': x_values, 'y': y_values, 'mode': 'markers'}

def scatter_plot(traces):
    plotly.offline.iplot(traces)
