"""
Course 4
Week 1 Practice Project
Load a county-level map of the USA and and draw it using matplotlib
"""

import matplotlib.pyplot as plt

USA_SVG_SIZE = [555, 352]
HOUSTON_POS = [302, 280]


def draw_usa_map(map):
    """
    :param map: png file location (as string)
    :return: a drawn map
    """
    # Load map image, note that using 'rb'option in open() is critical since png files are binary
    with open(map, 'rb') as the_map_file:
        the_map_img = plt.imread(the_map_file)

    #  Get dimensions of USA map image
    ypixels, xpixels, bands = the_map_img.shape

    # Plot USA map
    plot_img = plt.imshow(the_map_img)

    # Plot green scatter point in center of map
    plt.scatter(x=xpixels / 2,
                y=ypixels / 2,
                s=100,
                c='Green')

    # Plot red scatter point on Houston, Tx - include code that rescale coordinates for larger PNG files
    plt.scatter(x=HOUSTON_POS[0] * xpixels / USA_SVG_SIZE[0],
                y=HOUSTON_POS[1] * ypixels / USA_SVG_SIZE[1],
                s=100,
                c='Red')

    plt.show()

draw_usa_map('/Users/timothyeason/Desktop/test_files/Course 4/Week 1 Project Files/USA_Counties_555x352.png')
