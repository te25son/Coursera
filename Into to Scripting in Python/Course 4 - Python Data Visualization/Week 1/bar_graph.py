"""
practice building bar graphs
"""

import pygal
import random


def make_bar_graph(title, xvals, data1, data2=None, data3=None, data4=None):
    """
    Input:
        title: string
        xvals: iterable
        data1: list where first element is string type and second element is list type
        data2: same as data1
        ...
    
    Return:
        returns a bar graph to the browser
    """
    # build the bar graph
    bar_graph = pygal.Bar()
    
    # add the title
    bar_graph.title = title
    
    # add the x-axis
    bar_graph.x_labels = xvals
    
    # add the data
    bar_graph.add(data1[0], data[1])
    
    if data2:
        bar_graph.add(data2[0], data2[1])
        
    # render the bar graph
    bar_graph.render_in_brower()
    
    
x_values = map(str, range(1999, 2011))
my_data = ['data', [
    random.randrange(0, 50) for x in range(12)
]]
my_other_data = ['more data', [
    random.randrange(0, 50) for x in range(12)
]]

make_bar_graph('my first bar graph', x_values, my_data, my_other_data)
