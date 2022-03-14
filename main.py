"""
This is the start of the exercise-app project.
Below is a simple 'Hello World' script for testing.
This will validate that Pycharm is working locally on your device
and Github our version control system is syncing properly.
The console bellow should print 'Hi, Group!'
"""

#  required  packages to implement this part:  pip  pandas  xlrd  openpyxl
#  to install  >    Ctrl + Alt + S   >   (+)  to ADD PACKAGES
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('Group!')

#  function returning a set of columns of file provided as parameter
def read_file_to_variable(file_name):
    # read excel file
    xls = pd.ExcelFile(file_name)
    # df variable to store file content
    df = pd.read_excel(xls, "MetasoftStudio")

    # Select Columns from xls file
    selected_columns = df[["V'O2", "V'O2/kg", "V'O2/HR", "V'CO2", "HR", "WR"]]
    return selected_columns

breath_data_from_file = read_file_to_variable("Copy_of_CPET_DM01__Max_Breath_by_Breath.xlsx")
vo2 = breath_data_from_file[["V'O2"]]
vo2kg = breath_data_from_file[["V'O2/kg"]]
vo2hr = breath_data_from_file[["V'O2/HR"]]
vco2 = breath_data_from_file[["V'CO2"]]
hr = breath_data_from_file[["HR"]]
wr = breath_data_from_file[["WR"]]


print(breath_data_from_file)

print(type(breath_data_from_file))

print(vo2)
print(vo2kg)
print(vo2hr)
print(vco2)
print(hr)
print(wr)

#  print(vo2)

plt.plot(breath_data_from_file)

