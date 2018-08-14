"""
Final Project for Week 2
------------------------
Creating Line Plots of GDP Data
"""

import csv
import pygal

CSV_FILE = 'isp_gdp.csv'


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    table = []

    with open(filename, newline='') as csv_file:

        csv_reader = csv.DictReader(csv_file,
                                    delimiter=separator,
                                    quotechar=quote)

        for row in csv_reader:
            table.append(row)

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
        if int(key) in year_range:
            if val != '':
                tup_list.append((int(key), float(val)))
            else:
                tup_list.append((int(key), None))

    return tup_list


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
    fin_dict = {}

    table = read_csv_as_list_dict(
        gdpinfo['gdpfile'],
        gdpinfo['separator'],
        gdpinfo['quote']
    )

    year_range = range(gdpinfo['min_year'], gdpinfo['max_year'] + 1)

    for row in table:
        fin_dict[row[gdpinfo['country_name']]] = {}
        for year in year_range:
            fin_dict[row[gdpinfo['country_name']]][str(year)] = 0

    for key in fin_dict:
        for row in table:
            if key == row[gdpinfo['country_name']]:
                for year in year_range:
                    fin_dict[key][str(year)] = row[str(year)]

    for key in fin_dict:
        fin_dict[key] = build_plot_values(gdpinfo, fin_dict[key])

    return fin_dict


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
    xy_chart = pygal.XY(title=u'Plot of GDP for select countries spanning 1960 to 2015',
                        x_title='Year',
                        y_title='GDP in USD')

    pass


gdpinfo = {
        "gdpfile": "isp_gdp.csv",        # Name of the GDP CSV file
        "separator": ",",                # Separator character in CSV file
        "quote": '"',                    # Quote character in CSV file
        "min_year": 1960,                # Oldest year of GDP data in CSV file
        "max_year": 2015,                # Latest year of GDP data in CSV file
        "country_name": "Country Name",  # Country name field name
        "country_code": "Country Code"   # Country code field name
    }

the_table = read_csv_as_list_dict(CSV_FILE, gdpinfo['separator'], gdpinfo['quote'])
