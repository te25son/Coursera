"""
PROJECT - WORKING WITH NUMBERS
------------------------------
Project for Coursera week 4
"""

import datetime


def days_in_month(year, month):
    """
    Takes the parameters year and month and returns the number of days in the given month.
    """
    date1 = datetime.date(year, month, 1)
    year1 = date1.year
    month1 = date1.month
    if date1.month == 12:
        year2 = date1.year + 1
        month2 = 1
        date2 = datetime.date(year2, month2, 1)
        difference_days = date2 - date1
        return difference_days.days
    else:
        month2 = month1 + 1
        date2 = datetime.date(year1, month2, 1)
        difference_days = date2 - date1
        return difference_days.days


def is_valid_date(year, month, day):
    """
    Takes the parameters year, month, and day and returns True if year-month-day
    is a valid date and False otherwise.
    """
    if (year <= datetime.MAXYEAR and year >= datetime.MINYEAR) and (month >= 0 and month <= 12) and \
            (day > 0 and day <= days_in_month(year, month)):
        return True
    else:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Takes the parameters year, month and day for two dates and returns the difference
    in days.
    """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        if date2 >= date1:
            difference = date2 - date1
            return difference.days
        else:
            return 0
    else:
        return 0


def age_in_days(year, month, day):
    """
    Takes the parameters year, month, and day and returns the difference between
    the given date and today.
    """
    todays_date = datetime.date.today()
    date1 = datetime.date(year, month, day)
    if is_valid_date(year, month, day) and date1 <= todays_date:
        return days_between(year, month, day, todays_date.year, todays_date.month, todays_date.day)
    else:
        return 0
