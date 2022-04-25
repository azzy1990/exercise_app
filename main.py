"""
This is the start of the exercise-app project.
Below is a simple 'Hello World' script for testing.
This will validate that Pycharm is working locally on your device
and Github our version control system is syncing properly.
The console bellow should print 'Hi, Group!'
"""
#  required  packages to implement this part:  pip  pandas  xlrd  openpyxl matplotlib.pyplot pyex
#  to install  >    Ctrl + Alt + S   >   (+)  to ADD PACKAGES
from tkinter import filedialog, Tk

import numpy
import pandas as pd
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import numpy as np
from scipy.interpolate import make_interp_spline

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
    selected_columns = df[["t", "V'O2", "V'O2/kg", "V'O2/HR", "V'CO2", "HR", "WR", "V'E"]]
    return selected_columns

# Loading bitmap
napier_logo_bitmap = Image.open('Edinburgh-Napier-logo-1000.png')

def chart(breath_data_from_file):  # breathe file loading and extracting columns into
    time_raw = breath_data_from_file["t"]
    # trim the time strings first 2 character  and 4 last
    time = [item[2:-4] for item in time_raw]
    vo2 = breath_data_from_file["V'O2"]
    vo2kg = breath_data_from_file["V'O2/kg"]
    vo2hr = breath_data_from_file["V'O2/HR"]
    vco2 = breath_data_from_file["V'CO2"]
    hr = breath_data_from_file["HR"]
    wr = breath_data_from_file["WR"]
    vee = breath_data_from_file["V'E"]

    def plot_setup_insert_logo():
        plt.margins(x=0, y=0)
        plt.grid(alpha=0.37)
        plt.gca().spines['right'].set_color('0.85')
        plt.gca().spines['top'].set_color('0.85')
        plt.gca().spines['bottom'].set_color('0.5')
        plt.gca().spines['left'].set_color('0.5')
        newax = fig.add_axes([0.75, 0.75, 0.235, 0.235], anchor='NE', zorder=1)
        newax.imshow(napier_logo_bitmap)
        newax.axis('off')

    # Drawing   VCO2 /  VO2  graph
    fig, ax = plt.subplots()
    plt.scatter(vo2, vco2, alpha=0.8, s=50, linewidths=0.05)
    plt.xlim(left=1, right=4.2)
    plt.ylim(bottom=1)
    plt.title("Gas Exchange", fontsize=19, loc='left', y=1.02)
    plt.xlabel("VO2 (L/min)", fontsize=16)
    plt.ylabel("VCO2  (L/min)", fontsize=16)
    # placing the Napier logo in right top corner
    plot_setup_insert_logo()
    # plt.show()
    plt.savefig("chart__1.png", dpi=140)

    # Drawing   VE  /  VO2  graph
    fig, ax = plt.subplots()
    plt.scatter(vo2, vee, alpha=0.8, s=50, linewidths=0.05)
    plt.xlim(left=1, right=4.2)
    # plt.ylim(bottom=1)
    plt.title("VO2 / VE", fontsize=19, loc='left', y=1.02)
    plt.xlabel("VO2  (L/min)", fontsize=16)
    plt.ylabel("VE  (L/min)", fontsize=16)
    # placing the Napier logo in right top corner
    plot_setup_insert_logo()
    # plt.show()
    plt.savefig("chart__2.png", dpi=140)

    # Drawing  VO2 MAX  graph
    fig, ax = plt.subplots()
    plt.scatter(time, vo2, alpha=0.8, s=30)
    plt.tick_params(axis='x', which='major', labelsize=8)
    plt.xticks(np.arange(0, 500, 18))
    plt.ylim(bottom=1)
    plt.xlabel("time (Min:Seconds)", fontsize=16)
    plt.ylabel("VO2  (L/min)", fontsize=16)
    plt.title("VO2 Max", fontsize=19, loc='left', y=1.02)
    # placing the Napier logo in right top corner
    plot_setup_insert_logo()
    # plt.show()
    plt.savefig("chart__3.png", dpi=140)

    # drawing  Maximal Oxygen Uptake (VO2 Max)
    fig, ax = plt.subplots()
    plt.scatter(wr, vo2, alpha=0.8, s=30)
    plt.tick_params(axis='x', which='major', labelsize=8)
    plt.ylim(bottom=1)
    plt.xlabel("Work Rate (W)", fontsize=16)
    plt.ylabel("VO2  (L/min)", fontsize=16)
    plt.title("Maximal Oxygen Uptake (VO2 Max)", fontsize=15, loc='left', y=1.02)
    # placing the Napier logo in right top corner
    plot_setup_insert_logo()
    # plt.show()
    plt.savefig("chart__4.png", dpi=140)

    # drawing   Heart rate / Work Rate" graph
    fig, ax = plt.subplots()
    plt.scatter(wr, hr, alpha=0.8, s=40, linewidths=0.05)
    plt.title("Heart rate", fontsize=19, loc='left', y=1.02)
    plt.xlabel("Work Rate (W)", fontsize=14)
    plt.ylabel("Heart rate (Beats/ Min)", fontsize=14)
    # placing the Napier logo in right top corner
    plot_setup_insert_logo()
    # plt.show()
    plt.savefig("chart__5.png", dpi=140)

#  Created by Alexandru
import eel
eel.init("web")
# @eel.expose
# def py_fnct( strn ):
#    print( strn )
@eel.expose
def upload():
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    uploaded_file = filedialog.askopenfile()
    chart(read_file_to_variable(uploaded_file.name))

eel.start('main.html', block=False)  # starts the python web server

# eel.js_fnct( "String was printed" ) # has to be in the js code, exposed and declared

while True:  # keeps the server running
    eel.sleep(10)


"""   ------  PLOTS WITH AVERAGES
# functino to calculate rolling average
# x == an array of data. N == number of samples per average
def running_mean(x, N):
    cumsum = numpy.cumsum(numpy.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / float(N)


# drawing   VCO2 /  VO2  graph
fig, ax = plt.subplots()
# sorting lists
# vo2_sorted = sorted(vo2)
# vco2_sorted = sorted(vco2)
# calculate rolling average
# vo2_sorted_rolling_average  = running_mean(vo2_sorted, 27)
# vco2_sorted_rolling_average = running_mean(vco2_sorted, 27)
# rolling average lines
# plt.plot(vo2_sorted_rolling_average, vco2_sorted_rolling_average, linewidth=6.4, color="white")
# plt.plot(vo2_sorted_rolling_average, vco2_sorted_rolling_average, linewidth=2, color="deeppink")
plt.scatter(vo2, vco2, alpha=0.75, s=50, linewidths=0.05, edgecolors=None)
plt.xlim([1, 4])
plt.ylim(bottom=1)
#plt.gca().spines['top'].set_visible(False)
plt.title("Gas Exchange", fontsize=19, loc='left')
plt.xlabel("VCO2 (L/min)", fontsize=16)
plt.ylabel("VO2  (L/min)", fontsize=16)
#placing the Napier logo in right top corner
plot_setup_insert_logo()
plt.show()

# drawing   Heart rate / Work Rate" graph
fig, ax = plt.subplots()
# sorl lists
# vo2_sorted = sorted(vo2)
# hr_sorted = sorted(hr)
# calculate rolling averages
# vo2_sorted_rolling_average  = running_mean(vo2_sorted, 30)
# hr_sorted_rolling_average = running_mean(hr_sorted, 30)
# rolling average lines
# pl.plot(vo2_sorted_rolling_average, hr_sorted_rolling_average, linewidth=6.42, color="white")
# plt.plot(vo2_sorted_rolling_average, hr_sorted_rolling_average, linewidth=2, color="deeppink")
plt.scatter(wr, hr, alpha=0.7, s=40, linewidths=0.05)
# plt.xlim([1, 4])
# plt.ylim([1, 4.5])
plt.title("Heart rate / Work Rate", fontsize=19, loc='left')
plt.xlabel("Work Rate (W)", fontsize=16)
plt.ylabel("Heart rate (Beats/ Min)", fontsize=16)
#placing the Napier logo in right top corner
plot_setup_insert_logo()
plt.show()
"""
