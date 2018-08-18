"""
Some code to illustrate the speed of the 'in' operator
for lists vs. dictionaries in Python
"""

import time
import csv
import random


def read_csv_file(filename):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Nested list consisting of the fields in the CSV file
    """
    with open(filename, newline='') as csv_file:
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            csv_table.append(row)

    return csv_table


CANCER_RISK_FIPS_COL = 2
CENTER_FIPS_COL = 0
