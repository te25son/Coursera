"""
Examples of drawing line plots with pygal
"""

import pygal
import random


def draw_line(title, xvals, yvals, yvals2=None, yvals3=None):
    """
    Draws a line plot with the given title and x and y values
    """
    # create line plot on which we'll put our data
    line_plot = pygal.Line(height=400)

    # set the title to what you want
    line_plot.title = title

    # label the x axis with the given x values
    line_plot.x_labels = xvals

    # add the sequence of data you want to plot
    line_plot.add('Data', yvals)

    if yvals2:
        line_plot.add('More_Data', yvals2)

        if yvals3:
            line_plot.add('Even More Data', yvals3)

    # show the line plot
    line_plot.render_in_browser()


x_values_str = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

example_x_values = [0, 1, 3, 5, 6, 7, 9, 11, 12, 15, 16, 19]

x_values_num = [
    num for num in range(24) if num % 2 == 0
]

random_x_values = [
    random.randrange(0, 24) for x in range(12)
]

y_values = [4, 3, 1, 2, 2, 4, 5, 2, 1, 4, 7, 9]

more_y_values = [7, 10, 9, 4, 6, 1, 7, 8, 7, 7, 6, 2]

even_more_y_values = [
    random.randrange(0, 16) for x in range(12)
]

# draw_line("My First Line Plot", x_values_str, y_values, more_y_values, even_more_y_values)


def draw_xy(title, xvals, yvals, more_x=None, more_y=None):
    """
    Draws an XY (scatter) plot with the given title, x and y values
    """
    # provide x and y values as a sequence of tuples
    # so pygal knows where you want them placed (doesn't assume you want them spaced evenly)
    coords = [
        (xval, yval) for xval, yval in zip(xvals, yvals)
    ]

    # create the XY plot
    xyplot = pygal.XY(stroke=False, height=400)  # stoke tells whether you want the dots connected by a line or not

    # give your plot its title
    xyplot.title = title

    # add the data to the XY plot
    xyplot.add('Data', coords)

    if more_x and more_y:
        xyplot.add('More Data', [
            (xval, yval) for xval, yval in zip(more_x, more_y)
        ])

    #show the XY plot
    xyplot.render_in_browser()


# draw_xy('My XY Plot', example_x_values, y_values, random_x_values, even_more_y_values)
