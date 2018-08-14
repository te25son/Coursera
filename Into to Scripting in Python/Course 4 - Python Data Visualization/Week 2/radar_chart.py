"""
Practice creating a radar chart
"""

import pygal
from pygal.style import LightSolarizedStyle


def make_radar_chart(title, data_title, data):
    """
    Input:
    	title: string
        data_title: string
        data: dictionary whereby the keys will be the x-axis and the values the
        data to be plotted
        
    Output:
        returns a radar chart to the browser
    """
    # make the chart
    radar_chart = pygal.Radar(fill=True, style=LightSolarizedStyle)
    
    # add the title
    radar_chart.title = title
    
    # add the x-axis values
    radar_chart.x_labels = [item for item in data]
    
    # add the data
    radar_chart.add(
        data_title,
        [data[item] for item in data]
    )
    
    #return the radar chart
    radar_chart.render_in_browser()


my_dict = {
    'Career / Business': 10,
    'Finance': 4,
    'Spirituality': 5,
    'Personal Growth': 9,
    'Quality of Life': 7,
    'Fitness / Sport': 8,
    'Friends / Environment': 2,
    'Relationship': 7
}
    
make_radar_chart('Life Circle', 'Tim', my_dict)
