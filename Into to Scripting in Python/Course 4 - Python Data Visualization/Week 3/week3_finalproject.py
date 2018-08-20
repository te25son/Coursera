"""
Final Project for Week 3
"""


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
