"""
Final Project for Week 2
------------------------
Creating Line Plots of GDP Data
"""

import csv
import pygal


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}

    with open(filename, 'rt', newline='') as csv_file:

        csv_reader = csv.DictReader(csv_file,
                                    delimiter=separator,
                                    quotechar=quote)

        for row in csv_reader:
            table[row[keyfield]] = row

    return table


def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.

    Output:
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    tup_list = []

    year_range = range(gdpinfo['min_year'], gdpinfo['max_year'] + 1)

    for key, val in gdpdata.items():
        try:
            if int(key) in year_range:
                if val != '':
                    tup_list.append((int(key), float(val)))

        except ValueError:
            return tup_list

    sorted_tup_list = sorted(tup_list, key=lambda tup: tup[0])

    return sorted_tup_list


def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """
    master_dict = {}

    table = read_csv_as_nested_dict(
        gdpinfo['gdpfile'],
        gdpinfo['country_name'],
        gdpinfo['separator'],
        gdpinfo['quote']
    )

    year_range = range(gdpinfo['min_year'], gdpinfo['max_year'] + 1)

    for key in table:
        if key in country_list:
            master_dict[key] = {}
            for year in year_range:
                master_dict[key][str(year)] = table[key][str(year)]

        else:
            for country in country_list:
                if country not in table.keys():
                    master_dict[country] = []

    for key in master_dict:
        if master_dict[key] != []:
            master_dict[key] = build_plot_values(gdpinfo, master_dict[key])

    return master_dict


def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by info for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """
    xy_chart = pygal.XY(height=400,
                        title=u'Plot of GDP for select countries spanning 1960 to 2017',
                        x_title='Year',
                        y_title='GDP in USD',
                        show_dots=False)

    plot_dict = build_plot_dict(gdpinfo, country_list)

    for key, value in plot_dict.items():
        xy_chart.add(key, value)

    # xy_chart.render_to_file(plot_file)

    xy_chart.render_in_browser()


def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
    """
    gdpinfo = {
        "gdpfile": "modern_gdp_data.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2017,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    # render_xy_plot(gdpinfo, [], "isp_gdp_xy_none.svg")
    # render_xy_plot(gdpinfo, ["China"], "isp_gdp_xy_china.svg")
    render_xy_plot(gdpinfo, ["United States", "European Union", "World"],
                   "isp_gdp_xy_uk+usa.svg")


# Make sure the following call to test_render_xy_plot is commented out
# when submitting to OwlTest/CourseraTest.

test_render_xy_plot()
