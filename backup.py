"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    with open(filename,newline='') as csvfile :
        csvreader = csv.DictReader(csvfile,
                                        delimiter=separator,
                                        quotechar=quote)


    return csvreader.fieldnames

# print(read_csv_fieldnames("hightemp.csv", ',', '"' ))


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
    with open(filename, newline='') as csvfile :
        csvreader = csv.DictReader(csvfile, delimiter=separator,
                                            quotechar=quote)

        for row in csvreader :
            table.append(row)
    return table


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
    table={}
    with open(filename) as csvfile :
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)

        for row in csvreader :
            table[row[keyfield]]= row
    return table


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    update=[]
    with open(filename, 'w', newline='') as csvfilew :
        csv_writer = csv.writer(csvfilew, delimiter=separator,quoting=quote)
        for row in table :
            update.append(row)

        csv_writer.writerow(fieldnames)
        for row in update:
            value=[]
            for field in fieldnames :
                value.append(row[field])
            csv_writer.writerow(value)

# write_csv_from_list_dict('output1.csv', [{'b': 11, 'c': 12, 'd': 13, 'a': 10, 'e': 14}, {'b': 21, 'c': 22, 'd': 23, 'a': 20, 'e': 24}, {'b': 31, 'c': 32, 'd': 33, 'a': 30, 'e': 34}, {'b': 41, 'c': 42, 'd': 43, 'a': 40, 'e': 44}], ['a', 'b', 'c', 'd', 'e'], ',', '"')
