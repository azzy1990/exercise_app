"""
This is the start of the exercise-app project.
Below is a simple 'Hello World' script for testing.
This will validate that Pycharm is working locally on your device
and Github our version control system is syncing properly.
The console bellow should print 'Hi, Group!'
"""

#  required  packages to implement this part:  pip  pandas  xlrd  openpyxl matplotlib.pyplot
#  to install  >    Ctrl + Alt + S   >   (+)  to ADD PACKAGES
import pandas as pd
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
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
    selected_columns = df[["t", "V'O2", "V'O2/kg", "V'O2/HR", "V'CO2", "HR", "WR"]]
    return selected_columns

breath_data_from_file = read_file_to_variable("Copy_of_CPET_DM01__Max_Breath_by_Breath.xlsx")
time = breath_data_from_file["t"]
vo2 = breath_data_from_file["V'O2"]
vo2kg = breath_data_from_file["V'O2/kg"]
vo2hr = breath_data_from_file["V'O2/HR"]
vco2 = breath_data_from_file["V'CO2"]
hr = breath_data_from_file["HR"]
wr = breath_data_from_file["WR"]

# print(breath_data_from_file)
# print(vo2)
#  reading bitmaps
napier_logo_bitmap = Image.open('Edinburgh-Napier-logo-1000.png')
bitmap_height = napier_logo_bitmap.size[0]
bitmap_width = napier_logo_bitmap.size[1]
# napier_logo_bitmap = np.array(napier_logo_bitmap).astype(np.float)/255
fig = plt.figure()
#plt.rcParams['figure.dpi'] = 100
plt.scatter(vo2, vco2, alpha=0.7, s=30)
plt.margins(x=0, y=0)
plt.title("V'O2 / V'CO2", fontsize=22)
plt.xlabel("V'O2", fontsize=17)
plt.ylabel("V'CO2", fontsize=17)
fig.figimage(napier_logo_bitmap, fig.bbox.xmax - bitmap_height, fig.bbox.ymax )
plt.show()

fig = plt.figure()
plt.scatter(vo2, hr, alpha=0.7, s=30)
plt.title("V'O2 / Heart rate", fontsize=22)
plt.xlabel("V'O2", fontsize=17)
plt.ylabel("Heart rate", fontsize=17)
fig.figimage(napier_logo_bitmap, fig.bbox.xmax - bitmap_height, fig.bbox.ymax )
plt.show()
