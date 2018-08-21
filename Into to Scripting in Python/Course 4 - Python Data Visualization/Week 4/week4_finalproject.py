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
        master_dict[key] = table[key]['data_codes']
        
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
    
    pass
