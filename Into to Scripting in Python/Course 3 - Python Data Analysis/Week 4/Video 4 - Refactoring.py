"""
Course 3
Week 4 - Video 4 - Refactoring
"""

# refactoring = cleaning up your code so others can read it more easily

# converting the average daily temperatures on several planets
# from Kelvin to Fahrenheit

MERCURY_KELVIN = 440
VENUS_KELVIN = 737
MARS_KELVIN = 210
EARTH_KELVIN = 288


def kelvin_to_celsius(temp):
    """
        Converts a temperature in kelvin to celsius
        and returns the temperature in celsius
    """
    return temp - 273.15  # -273.15 celsius = 0 kelvin


def kelvin_to_fahrenheit(temp):
    """
        Converts a temperature in kelvin to fahrenheit
        and returns the temperature in fahrenheit
    """
    return kelvin_to_celsius(temp) * 9 / 5 + 32  # the formula for converting celsius to fahrenheit


def display_text(planet, temp, temp_scale):
    """
        Displays text of the planet name (str), the average temperate (int),
        and the temperature scale (Fahrenheit or Celsius) (str)
    """
    temp = '{0:.2f}'.format(temp)
    return 'The average daily temperature on {} is apx. {} degrees {}'.format(
        planet, temp, temp_scale
    )


# test functions
merc_fahren = kelvin_to_fahrenheit(MERCURY_KELVIN)
merc_cels = kelvin_to_celsius(MERCURY_KELVIN)
print(display_text('Mercury', merc_cels, 'Celcius'))
print(display_text('Mercury', merc_fahren, 'Fahrenheit'))
print('')
mars_fahren = kelvin_to_fahrenheit(MARS_KELVIN)
mars_cels = kelvin_to_celsius(MARS_KELVIN)
print(display_text('Mercury', mars_cels, 'Celcius'))
print(display_text('Mercury', mars_fahren, 'Fahrenheit'))
print('')
earth_fahren = kelvin_to_fahrenheit(EARTH_KELVIN)
earth_cels = kelvin_to_celsius(EARTH_KELVIN)
print(display_text('Earth', earth_cels, 'Celsius'))
print(display_text('Earth', earth_fahren, 'Fahrenheit'))