"""
Final Project for Week 4
Final Project for this course and specialization :-(
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


def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """
    master_dict = {}
    
    table = read_csv_as_nested_dict(
        codeinfo['codefile'], 
        codeinfo['plot_codes'], 
        codeinfo['separator'], 
        codeinfo['quote']
    )
    
    for key in table:
        master_dict[key] = table[key][codeinfo['data_codes']]
        
    return master_dict


def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.

      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    master_dict = {}
    master_set = set()
    
    code_dict = build_country_code_converter(codeinfo)

    code_lower = {
        key.lower(): value.lower() for key, value in code_dict.items()
    }
    gdp_lower = {
        key.lower(): key for key in gdp_countries
    }

    for key in plot_countries:

        if key.lower() in code_lower:
            value = code_lower[key.lower()]

            if value in gdp_lower:
                value = gdp_lower[value]
                master_dict[key] = value

            else:
                master_set.add(key)

        else:
            master_set.add(key)

    return master_dict, master_set


def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

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
        gdpinfo['country_code'],
        gdpinfo['separator'],
        gdpinfo['quote']
    )

    country_codes = reconcile_countries_by_code(codeinfo, plot_countries, table)

    for key, value in country_codes[0].items():
        if table[value][year] != '':
            master_dict[key] = math.log(float(table[value][year]), 10)
        else:
            no_gdp_set.add(key)

    return master_dict, country_codes[1], no_gdp_set


def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """
    worldmap = pygal.maps.world.World()

    worldmap.title = "GDP of World Countries in " + year

    three_tups = build_map_dict_by_code(
        gdpinfo, codeinfo, plot_countries, year
    )

    worldmap.add('GDP in ' + year, three_tups[0])
    worldmap.add('No World Bank Data', three_tups[1])
    worldmap.add('No GDP in ' + year, three_tups[2])

    worldmap.render(map_file)


def test_render_world_map():
    """
    Test the project code for several years
    """
    gdpinfo = {
        "gdpfile": "/Users/timothyeason/Desktop/isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    codeinfo = {
        "codefile": "/Users/timothyeason/Desktop/isp_country_codes.csv",
        "separator": ",",
        "quote": '"',
        "plot_codes": "ISO3166-1-Alpha-2",
        "data_codes": "ISO3166-1-Alpha-3"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1960", "isp_gdp_world_code_1960.svg")

    # 1980
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")

    # 2000
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")

    # 2010
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

# test_render_world_map()
