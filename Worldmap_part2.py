"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, newline='', encoding="utf-8") as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
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
    return_dict = {}
    datafile = read_csv_as_nested_dict(codeinfo['codefile'],
    codeinfo['plot_codes'], codeinfo['separator'], codeinfo['quote'])

    for plot_code in datafile :
        return_dict[plot_code] = datafile[plot_code][codeinfo['data_codes']]

    return return_dict


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

    return_dict = {}
    return_set = set()
    lowered_data = {}
    lowered_gdp_data = {}
    # plot to data
    converter = build_country_code_converter(codeinfo)
    # make a dictionary that maps converter's key in lower caser to upper caser
    for each in converter :
        lowered_data[each.casefold()] = each

    for each in gdp_countries :
        lowered_gdp_data[each.casefold()] = each


    # print("lowered_data :", lowered_data)
    # print("converter :", converter)
    # print("plot_countries :", plot_countries)
    # print("gdp countries :", gdp_countries)
    # print("lowered_gdp_data :", lowered_gdp_data)


    # ✅THIS IS SUPER MESS. I HAVE TO CLEAR IT UP✅
    for plot_code in plot_countries :
        # print("plot_code:", plot_code)
        # if plot_countries[plot_code] in converter :
        if plot_code.casefold() in lowered_data:

            if lowered_data[plot_code.casefold()] in converter :

                if (converter[lowered_data[plot_code.casefold()]]).casefold() in lowered_gdp_data :
            # if converter[lowered_data[plot_code.lower()]] in gdp_countries :

                    return_dict[plot_code] = lowered_gdp_data[
                    (converter[lowered_data[plot_code.casefold()]]).casefold()]

                else :
                    return_set.add(plot_code)
            else :
                return_set.add(plot_code)
        else :
            return_set.add(plot_code)

    return return_dict, return_set

# print(reconcile_countries_by_code({'quote': '"',
# 'codefile': 'pygalproject/isp_code_csv_files/code4.csv',
# 'plot_codes': 'ISO3166-1-Alpha-2', 'separator': ','
# , 'data_codes': 'ISO3166-1-Alpha-3'},
# {'pr': 'Puerto Rico', 'no': 'Norway', 'us': 'United States'},
# {'NOR': {'Country Code': 'NOR', 'Country Name': 'Norway'},
# 'PRI': {'Country Code': 'PRI', 'Country Name': 'Puerto Rico'},
#  'USA': {'Country Code': 'USA', 'Country Name': 'United States'}}))
# print(reconcile_countries_by_code({'codefile': 'pygalproject/isp_code_csv_files/code4.csv',
#  'data_codes': 'ISO3166-1-Alpha-3',
#  'plot_codes': 'ISO3166-1-Alpha-2', 'quote': '"', 'separator': ','},
#   {'no': 'Norway', 'pr': 'Puerto Rico', 'us': 'United States'},
#    {'USA': {'Country Name': 'United States', 'Country Code': 'USA'},
#  'NOR': {'Country Name': 'Norway', 'Country Code': 'NOR'}}))

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
    return_dict = {}
    return_set1 , return_set2 = set(), set()
    # test = reconcile_countries_by_code(codeinfo, plot_countries, gdpdata)
    gdpdata = read_csv_as_nested_dict(gdpinfo['gdpfile'], gdpinfo['country_code'],
     gdpinfo['separator'], gdpinfo['quote'])

    #
    # print(gdpdata)
    # print(gdpdata_by_year)
    # print(converter)
    # print(plot_countries)
    # print()
    existing, non_existing = reconcile_countries_by_code(codeinfo, plot_countries, gdpdata)
    # print(existing)
    # print(non_existing)
    # print()
    for each in non_existing :
        return_set1.add(each)

    for each in existing :
        # print(each)
        if gdpdata[existing[each]][year] :
            # print(gdpdata[existing[each]][year])
            return_dict[each] = math.log10(float(gdpdata[existing[each]][year]))
        else :
            return_set2.add(each)

    return tuple((return_dict, return_set1, return_set2))

# print(build_map_dict_by_code({'min_year': 2000, 'separator': ','
# , 'country_name': 'Country Name', 'max_year': 2005,
#  'gdpfile': 'pygalproject/isp_gdp_csv_files/gdptable1.csv',
#   'country_code': 'Code', 'quote': '"'},
#   {'codefile': 'pygalproject/isp_code_csv_files/code2.csv',
#    'data_codes': 'Cd3', 'plot_codes': 'Cd2', 'quote': "'",
#     'separator': ','}, {'C1': 'c1', 'C4': 'c4', 'C3': 'c3', 'C5': 'c5', 'C2': 'c2'},
#      '2001'))


# print(build_map_dict_by_code({'country_name': 'Country Name',
# 'quote': '"', 'separator': ',', 'max_year': 1958, 'min_year': 1953,
#  'gdpfile': 'pygalproject/isp_gdp_csv_files/gdptable2.csv', 'country_code': 'Code'},
#  {'quote': "'", 'codefile': 'pygalproject/isp_code_csv_files/code2.csv', 'plot_codes': 'Cd2',
#   'separator': ',', 'data_codes': 'Cd1'},
#  {'C2': 'c2', 'C5': 'c5', 'C3': 'c3', 'C1': 'c1', 'C4': 'c4'}, '1953'))

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

    resources = build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year)
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'GDP - country'
    worldmap_chart.add("GDP for {}".format(year),resources[0])
    worldmap_chart.add("Missing",resources[1])
    worldmap_chart.add("No GDP data",resources[2])

    worldmap_chart.render_in_browser()
    return


def test_render_world_map():
    """
    Test the project code for several years
    """
    gdpinfo = {
        "gdpfile": "visualization /isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    codeinfo = {
        "codefile": "visualization /isp_country_codes.csv",
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

test_render_world_map()
