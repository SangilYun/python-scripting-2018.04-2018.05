import csv



MONTHS = ('Jan', 'Feb', 'Mar', 'Apr',
          'May', 'Jun', 'Jul', 'Aug',
          'Sep', 'Oct', 'Nov', 'Dec')


def readfile(file_name) :
    table = []
    with open(file_name,"r", newline ='') as file_name:
        csvreader = csv.reader(file_name)
        for row in csvreader :
            table.append(row)
    return table


#my try
def print_table(table) :
    for row in table :
        for col in row[1:] :
            # print(row)
            print("{:<4}".format(col), end='')
        print(end='\n')

table = readfile("hightemp.csv")
# print_table(table)


#answer
def print_table(table):
    """
    Print out table, which must be a list
    of lists, in a nicely formatted way.
    """
    for row in table:
        # Header column left justified
        print("{:<19}".format(row[0]), end='')
        # Remaining columns right justified
        for col in row[1:]:
            print("{:>4}".format(col), end='')
        print("", end='\n')

table = readfile("hightemp.csv")
# print_table(table)


def dict_reader(filename, keyfield) :
    table ={}
    with open(filename,'r', newline='') as csvfile :
        csvreader = csv.DictReader(csvfile, skipinitialspace=True)

        for row in csvreader :
            table[row[keyfield]] = row

        return table
table = dict_reader("hightemp.csv", "City")
# print_table(table)



def print_table2(table):
    """
    Print out table, which must be a dictionary
    of dictionaries, in a nicely formatted way.
    """
    print("City               ", end='')
    for month in MONTHS:
        print("{:>6}".format(month), end='')
    print("")
    for name, row in table.items():
        # Header column left justified
        print("{:<19}".format(name), end='')
        # Remaining columns right justified
        for month in MONTHS:
            print("{:>6}".format(row[month]), end='')
        print("", end='\n')

# table = dictparse("hightemp.csv", 'City')
print_table2(table)
