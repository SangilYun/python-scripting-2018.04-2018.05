"""
Converting the average daily temperatures for several planets
from Kelvin to Farenheit --- Version 0
"""


# Initialize emperatures for various planets
# http://www.smartconversion.com/otherInfo/Temperature_of_planets_and_the_Sun.aspx
mercury = 440
venus = 737
mars = 210

# Compute temperature in Farenheit
mercury_result = (mercury - 275.15) * 9 / 5 + 32
venus_result = (venus - 275.15) * 9 / 5 + 32
mars_result = (mars - 275.15) * 9 / 5 + 32

# Print
print("The daily average temperature on Mercury is", mercury_result, "Farenheit")
print("The daily average temperature on Venus is", venus_result, "Farenheit")
print("The daily average temperature on Mars is", mars_result, "Farenheit")

# Output
##The daily average temperature on Mercury is 328.73 Farenheit
##The daily average temperature on Venus is 863.33 Farenheit
##The daily average temperature on Mars is -85.27 Farenheit

#================================================================================

"""
Converting the average daily temperatures for several planets
from Kelvin to Farenheit --- Version 1
"""


# Initialize temperatures for various planets
# http://www.smartconversion.com/otherInfo/Temperature_of_planets_and_the_Sun.aspx
mercury = 440
venus = 737
mars = 210

# Compute temperature in Farenheit
def compute_temp(temp):
    """
    Given a floating point temperature temp in Kelvin,
    return the corresponding temperature in Farenheit
    """
    return (temp - 275.15) * 9 / 5 + 32

mercury_result = compute_temp(mercury)
venus_result = compute_temp(venus)
mars_result = compute_temp(mars)

# Print out results
print("The daily average temperature on Mercury is", mercury_result, "Farenheit")
print("The daily average temperature on Venus is", venus_result, "Farenheit")
print("The daily average temperature on Mars is", mars_result, "Farenheit")

# Output
##The daily average temperature on Mercury is 328.73 Farenheit
##The daily average temperature on Venus is 863.33 Farenheit
##The daily average temperature on Mars is -85.27 Farenheit


#================================================================================



"""
Converting the average daily temperatures for several planets
from Kelvin to Farenheit --- Version 2
"""


# Initialize temperatures for various planets
# http://www.smartconversion.com/otherInfo/Temperature_of_planets_and_the_Sun.aspx
mercury = 440
venus = 737
mars = 210

# Compute temperature in Farenheit
def compute_temp(temp):
    """
    Given a floating point temperature temp in Kelvin,
    return the corresponding temperature in Farenheit
    """
    return (temp - 275.15) * 9 / 5 + 32

mercury_result = compute_temp(mercury)
venus_result = compute_temp(venus)
mars_result = compute_temp(mars)

# Print out results
def print_temp(planet, temp):
    """
    Print out the average daily temps
    """
    print("The daily average temperature on", planet, "is", temp, "Farenheit")

print_temp("Mercury", mercury_result)
print_temp("Venus", venus_result)
print_temp("Mars", mars_result)

# Output
##The daily average temperature on Mercury is 328.73 Farenheit
##The daily average temperature on Venus is 863.33 Farenheit
##The daily average temperature on Mars is -85.27 Farenheit
#================================================================================


"""
Converting the average daily temperatures for several planets
from Kelvin to Farenheit --- Version 3
"""


# Initialize temperatures for various planets
# http://www.smartconversion.com/otherInfo/Temperature_of_planets_and_the_Sun.aspx
mercury = 440
venus = 737
mars = 210

# Compute temperature in Farenheit
def compute_celsius(temp):
    """
    Given a floaring point temperature temp in Kelvin,
    return the corresponding temperature in Celsius
    """
    return temp - 275.15

def compute_farenheit(temp):
    """
    Given a floating point temperature temp in Kelvin,
    return the corresponding temperature in Farenheit
    """
    temp_celsius = compute_celsius(temp)
    return temp_celsius * 9 / 5 + 32

mercury_result = compute_farenheit(mercury)
venus_result = compute_farenheit(venus)
mars_result = compute_farenheit(mars)

# Print out results
def print_temp(planet, temp):
    """
    Print out the average daily temps
    """
    print("The daily average temperature on", planet, "is", temp, "Farenheit")

print_temp("Mercury", mercury_result)
print_temp("Venus", venus_result)
print_temp("Mars", mars_result)

# Output
##The daily average temperature on Mercury is 328.73 Farenheit
##The daily average temperature on Venus is 863.33 Farenheit
##The daily average temperature on Mars is -85.27 Farenheit


#================================================================================
#change variable more readable

"""
Converting the average daily temperatures for several planets
from Kelvin to Farenheit --- Version 4
"""


# Initialize temperatures for various planets
# http://www.smartconversion.com/otherInfo/Temperature_of_planets_and_the_Sun.aspx
MERCURY_KELVIN = 440
VENUS_KELVIN = 737
MARS_KELVIN = 210

# Compute temperature in Farenheit
def kelvin_to_celsius(temp_kelvin):
    """
    Given a floaring point temperature temp in Kelvin,
    return the corresponding temperature in Celsius
    """
    return temp_kelvin - 275.15

def kelvin_to_farenheit(temp_kelvin):
    """
    Given a floating point temperature temp in Kelvin,
    return the corresponding temperature in Farenheit
    """
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    return temp_celsius * 9 / 5 + 32

mercury_farenheit = kelvin_to_farenheit(MERCURY_KELVIN)
venus_farenheit = kelvin_to_farenheit(VENUS_KELVIN)
mars_farenheit = kelvin_to_farenheit(MARS_KELVIN)

# Print out results
def print_temp_farenheit(planet, temp_farenheit):
    """
    Print out the average daily temps in Farenheit
    """
    print("The daily average temperature on", planet, "is", temp_farenheit, "Farenheit")

print_temp_farenheit("Mercury", mercury_farenheit)
print_temp_farenheit("Venus", venus_farenheit)
print_temp_farenheit("Mars", mars_farenheit)

# Output
##The daily average temperature on Mercury is 328.73 Farenheit
##The daily average temperature on Venus is 863.33 Farenheit
##The daily average temperature on Mars is -85.27 Farenheit



"""
Converting the average daily temperatures for several planets
from Kelvin to Farenheit --- Version 5
"""

# Important constants
ZERO_KELVIN_IN_CELSIUS = -275.15
ZERO_CELSIUS_IN_FARENHEIT = 32
CELSIUS_TO_FARENHEIT_SCALING = 9 / 5

# Initialize temperatures for various planets
# http://www.smartconversion.com/otherInfo/Temperature_of_planets_and_the_Sun.aspx
MERCURY_KELVIN = 440
VENUS_KELVIN = 737
MARS_KELVIN = 210

# Compute temperature in Farenheit
def kelvin_to_celsius(temp_kelvin):
    """
    Given a floaring point temperature temp in Kelvin,
    return the corresponding temperature in Celsius
    """
    return temp_kelvin + ZERO_KELVIN_IN_CELSIUS

def kelvin_to_farenheit(temp_kelvin):
    """
    Given a floating point temperature temp in Kelvin,
    return the corresponding temperature in Farenheit
    """
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    return temp_celsius * CELSIUS_TO_FARENHEIT_SCALING + ZERO_CELSIUS_IN_FARENHEIT

mercury_farenheit = kelvin_to_farenheit(MERCURY_KELVIN)
venus_farenheit = kelvin_to_farenheit(VENUS_KELVIN)
mars_farenheit = kelvin_to_farenheit(MARS_KELVIN)

# Print out results
def print_temp_farenheit(planet, temp_farenheit):
    """
    Print out the average daily temps in Farenheit
    """
    print("The daily average temperature on", planet, "is", temp_farenheit, "Farenheit")

print_temp_farenheit("Mercury", mercury_farenheit)
print_temp_farenheit("Venus", venus_farenheit)
print_temp_farenheit("Mars", mars_farenheit)

# Output
##The daily average temperature on Mercury is 328.73 Farenheit
##The daily average temperature on Venus is 863.33 Farenheit
##The daily average temperature on Mars is -85.27 Farenheit



"""
Converting the average daily temperatures for several planets
from Kelvin to Farenheit --- Version 6
"""

# Important constants
ZERO_KELVIN_IN_CELSIUS = -275.15
ZERO_CELSIUS_IN_FARENHEIT = 32
CELSIUS_TO_FARENHEIT_SCALING = 9 / 5

# Initialize temperatures for various planets
# http://www.smartconversion.com/otherInfo/Temperature_of_planets_and_the_Sun.aspx
MERCURY_KELVIN = 440
VENUS_KELVIN = 737
MARS_KELVIN = 210

# Compute temperature in Farenheit
def kelvin_to_celsius(temp_kelvin):
    """
    Given a floaring point temperature temp in Kelvin,
    return the corresponding temperature in Celsius
    """
    return temp_kelvin + ZERO_KELVIN_IN_CELSIUS

def kelvin_to_farenheit(temp_kelvin):
    """
    Given a floating point temperature temp in Kelvin,
    return the corresponding temperature in Farenheit
    """
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    return temp_celsius * CELSIUS_TO_FARENHEIT_SCALING + ZERO_CELSIUS_IN_FARENHEIT


# Print out results
def print_temp_farenheit(planet, temp_farenheit):
    """
    Print out the average daily temps in Farenheit
    """
    print("The daily average temperature on", planet, "is", temp_farenheit, "Farenheit")


# Compute and print results
def compute_and_print_temperatures():
    """
    Compute the temeperatues for three planets in Farenheit
    """
    mercury_farenheit = kelvin_to_farenheit(MERCURY_KELVIN)
    venus_farenheit = kelvin_to_farenheit(VENUS_KELVIN)
    mars_farenheit = kelvin_to_farenheit(MARS_KELVIN)

    print_temp_farenheit("Mercury", mercury_farenheit)
    print_temp_farenheit("Venus", venus_farenheit)
    print_temp_farenheit("Mars", mars_farenheit)

compute_and_print_temperatures()

# Output
##The daily average temperature on Mercury is 328.73 Farenheit
##The daily average temperature on Venus is 863.33 Farenheit
##The daily average temperature on Mars is -85.27 Farenheit
