"""
Final Project for Week 3
"""

import csv
import math
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


def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    master_dict = {}
    master_set = set()

    for key, value in plot_countries.items():
        if plot_countries[key] in gdp_countries.keys():
            master_dict[key] = value
        else:
            master_set.add(key)

    return master_dict, master_set


def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    master_dict = {}
    no_gdp_set = set()

    table = read_csv_as_nested_dict(
        gdpinfo['gdpfile'],
        gdpinfo['country_name'],
        gdpinfo['separator'],
        gdpinfo['quote']
    )

    country_codes = reconcile_countries_by_name(plot_countries, table)

    for key, value in country_codes[0].items():
        if table[value][year] != '':
            master_dict[key] = math.log(float(table[value][year]), 10)
        else:
            no_gdp_set.add(key)

    return master_dict, country_codes[1], no_gdp_set


# gdpinfo = {
#         "gdpfile": "isp_gdp.csv",
#         "separator": ",",
#         "quote": '"',
#         "min_year": 1960,
#         "max_year": 2015,
#         "country_name": "Country Name",
#         "country_code": "Country Code"
#     }
#
# name_table = read_csv_as_nested_dict(
#         gdpinfo['gdpfile'],
#         gdpinfo['country_name'],
#         gdpinfo['separator'],
#         gdpinfo['quote']
# )
# year = '1960'
#
# print(math.log(int(name_table['Aruba']['2010']), 10))
#
# test_dict = {}
# test_set = set()
# test_set2 = set()
#
# my_countries = {'ABW': 'Aruba', 'USA': 'United States', 'Boom': 'Boom'}
# test_tup = reconcile_countries_by_name(my_countries, name_table)
# print(test_tup)
# for key, value in test_tup[0].items():
#     if name_table[value][year] != '':
#         test_dict[key] = math.log(float(name_table[value][year]), 10)
#     else:
#         test_set2.add(key)
#
# print(test_dict, test_tup[1], test_set2)
