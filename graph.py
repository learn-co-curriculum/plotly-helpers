import plotly
from plotly.offline import iplot

def trace(data, mode = 'markers'):
    x_values = list(map(lambda point: point['x'],data))
    y_values = list(map(lambda point: point['y'],data))
    return {'x': x_values, 'y': y_values, 'mode': mode}

def line_function_trace(line_function, x_values, mode = 'line'):
    y_values = list(map(lambda x: line_function(x), x_values))
    return {'x': x_values, 'y': y_values, 'mode': mode}

def plot(traces):
    plotly.offline.iplot(traces)
