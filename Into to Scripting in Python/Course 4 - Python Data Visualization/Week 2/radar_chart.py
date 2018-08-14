"""
Practice creating a radar chart
"""

import pygal


def make_radar_chart(title, xvals, data):
    """
    Input:
    	title: string
        xvals: list of strings
        data: list where first element is a string and second element a list of data
        
    Output:
    	returns a radar chart to the browser
    """
    # make the chart
    radar_chart = pygal.Radar()
    
    # add the title
    radar_chart.title = title
    
    # add the x-axis values
    radar_chart.x_labels = xvals
    
    # add the data
    radar_chart.add(data[0], data[1])
    
    #return the radar chart
    radar_chart.render_in_browser()
    

values = ['Career / Business', 'Finance', 'Spirituality', 'Personal Growth', 'Quality of Life',
          'Fitness / Sport', 'Friends / Environment', 'Relationship']

my_data = ['Tim', [10, 5, 6, 9, 7, 8, 2, 7]]
    
make_radar_chart('Life Circle', values, my_data)
