"""
Practice creating a radar chart
"""

import pygal
from pygal.style import LightSolarizedStyle


def make_radar_chart(title, data_title, data, data_title2=None, data2=None):
    """
    Input:
    	title: string
        data_title: string
        data: dictionary whereby the keys will be the x-axis and the values the
        data to be plotted
        ...
        
    Output:
        returns a radar chart to the browser
    """
    # make the chart
    # radar_chart = pygal.Radar(fill=True, style=LightSolarizedStyle, range=(0, 10))
    radar_chart = pygal.Radar(fill=True, range=(0, 10), show_dots=False)
    
    # add the title
    radar_chart.title = title
    
    # add the x-axis values
    radar_chart.x_labels = [item for item in data]

    # add the data
    radar_chart.add(
        data_title,
        [data[item] for item in data]
    )

    if data2:
        radar_chart.x_labels = [item for item in data2]

        radar_chart.add(
            data_title2,
            [data2[item] for item in data2]
        )

    #return the radar chart
    radar_chart.render_in_browser()


my_dict = {
    'Career / Business': 2,
    'Finance': 2,
    'Spirituality': 3,
    'Personal Growth': 5,
    'Quality of Life': 4,
    'Fitness / Sport': 4,
    'Friends / Environment': 0,
    'Relationship': 3
}

pupsik_dict = {
    'Career / Business': 2,
    'Finance': 1,
    'Spirituality': 4,
    'Personal Growth': 3,
    'Quality of Life': 3,
    'Fitness / Sport': 1,
    'Friends / Environment': 4,
    'Relationship': 6
}
    
make_radar_chart('Life Circle', 'Tim', my_dict, 'Nastya', pupsik_dict)
