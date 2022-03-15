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

# breathe file loading and extracting columns into
breath_data_from_file = read_file_to_variable("Copy_of_CPET_DM01__Max_Breath_by_Breath.xlsx")
time_raw = breath_data_from_file["t"]
# trim the time strings first 2 character  and 4 last
time = [item[2:-4] for item in time_raw]
vo2 = breath_data_from_file["V'O2"]
vo2kg = breath_data_from_file["V'O2/kg"]
vo2hr = breath_data_from_file["V'O2/HR"]
vco2 = breath_data_from_file["V'CO2"]
hr = breath_data_from_file["HR"]
wr = breath_data_from_file["WR"]

#  reading bitmaps
napier_logo_bitmap = Image.open('Edinburgh-Napier-logo-1000.png')

# drawing   VO2 /  VCO2  graph
fig, ax = plt.subplots()
plt.scatter(vo2, vco2, alpha=0.7, s=30)
plt.margins(x=0, y=0)
plt.grid(alpha=0.37)
plt.gca().spines['right'].set_color('0.85')
plt.gca().spines['top'].set_color('0.85')
plt.gca().spines['bottom'].set_color('0.5')
plt.gca().spines['left'].set_color('0.5')
#plt.gca().spines['top'].set_visible(False)
plt.title("V'O2 / V'CO2", fontsize=19, loc='left')
plt.xlabel("V'O2", fontsize=16, color=('0.5'))
plt.ylabel("V'CO2", fontsize=16, color=('0.5'))
#placing the Napier logo in right top corner
newax = fig.add_axes([0.75, 0.75, 0.235, 0.235], anchor='NE', zorder=1)
newax.imshow(napier_logo_bitmap)
newax.axis('off')
plt.show()


# drawing  HR / TIME  graph
fig, ax = plt.subplots()
plt.scatter(time, hr, alpha=0.7, s=30)
plt.grid(alpha=0.37)
plt.tick_params(axis='x', which='major', labelsize=8)
plt.xticks(np.arange(0, 400, 18))
plt.gca().spines['right'].set_color('0.85')
plt.gca().spines['top'].set_color('0.85')
plt.gca().spines['bottom'].set_color('0.5')
plt.gca().spines['left'].set_color('0.5')
plt.margins(x=0, y=0)
plt.xlabel("Time", fontsize=16, color=('0.5'))
plt.ylabel("Heart rate", fontsize=16,  color=('0.5'))
plt.title("Heart rate / Time", fontsize=19, loc='left')
#placing the Napier logo in right top corner
newax = fig.add_axes([0.75, 0.75, 0.235, 0.235], anchor='NE', zorder=1)
newax.imshow(napier_logo_bitmap)
newax.axis('off')
plt.show()

# drawing  VO2 / TIME graph
fig, ax = plt.subplots()
plt.scatter(time, vo2, alpha=0.7, s=30)
plt.grid(alpha=0.37)
plt.tick_params(axis='x', which='major', labelsize=8)
plt.xticks(np.arange(0, 400, 18))
plt.gca().spines['right'].set_color('0.85')
plt.gca().spines['top'].set_color('0.85')
plt.gca().spines['bottom'].set_color('0.5')
plt.gca().spines['left'].set_color('0.5')
plt.margins(x=0, y=0)
plt.xlabel("Time", fontsize=16, color=('0.5'))
plt.ylabel("V'O2", fontsize=16,  color=('0.5'))
plt.title("V'O2 / Time", fontsize=19, loc='left')
#placing the Napier logo in right top corner
newax = fig.add_axes([0.75, 0.75, 0.235, 0.235], anchor='NE', zorder=1)
newax.imshow(napier_logo_bitmap)
newax.axis('off')
plt.show()

# drawing   VO2 /  HR  graph
fig, ax = plt.subplots()
plt.scatter(vo2, hr, alpha=0.7, s=30)
plt.margins(x=0, y=0)
plt.grid(alpha=0.37)
plt.gca().spines['right'].set_color('0.85')
plt.gca().spines['top'].set_color('0.85')
plt.gca().spines['bottom'].set_color('0.5')
plt.gca().spines['left'].set_color('0.5')
plt.title("V'O2 / Heart rate", fontsize=19, loc='left')
plt.xlabel("V'O2", fontsize=16, color=('0.5'))
plt.ylabel("Heart rate", fontsize=16, color=('0.5'))
#placing the Napier logo in right top corner
newax = fig.add_axes([0.75, 0.75, 0.235, 0.235], anchor='NE', zorder=1)
newax.imshow(napier_logo_bitmap)
newax.axis('off')
plt.show()

