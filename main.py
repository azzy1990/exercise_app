"""
This is the start of the exercise-app project.
Below is a simple 'Hello World' script for testing.
This will validate that Python and its packages are functioning locally on your device
and Github our version control system is syncing properly.
The console bellow should print 'Hi, Group!'
"""
#  required  packages to implement this part:  pip  pandas  xlrd  openpyxl matplotlib.pyplot pyex
#  to install  >    Ctrl + Alt + S   >   (+)  to ADD PACKAGES
from tkinter import filedialog, Tk


import numpy
import MySQLdb 
import pandas as pd
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
from fpdf import FPDF
import numpy as np
from scipy.interpolate import make_interp_spline
import eel

print( "Application running ...." ); # at localhost:8000/home.html


def on_close(page, sockets): # attempt at keeping Eel on while going to another page
    print(page, 'closed')
    print('Still have sockets open to', sockets)

eel.init('web')




#  Done by Alexandru
class User: # same parameters as in the database
    def __init__ ( self, id, username, password, fullname, age, is_admin, email ):
        self.id = int( float( id ) );
        self.username = str( username );
        self.password = str( password );
        self.fullname = str( fullname );
        self.age = int( float( age ) );
        self.is_admin = int( float( is_admin ) );
        self.email = str( email );

    def strn ( self ): # used to later print the data, so developers can test functionalities
        return "User( id=" + str( self.id ) + ", username='" + self.username + "', password='" + self.password + "', fullname='" + self.fullname + "', age=" + str( self.age ) + ", is_admin=" + str( self.is_admin ) + ", email='" + self.email + "' ) "; 

class Talk: # same parameters as in the database
    def __init__ ( self, id, send_id, get_id, message ):
        self.id = int( float( id ) );
        self.send_id = int( float( send_id ) );
        self.get_id = int( float( get_id ) );
        self.message = str( message );

    def strn ( self ): # used to later print the data, so developers can test functionalities
        return "Talk( id=" + str( self.id ) + ", send_id=" + str( self.send_id ) + ", get_id=" + str( self.get_id ) + ", message='" + self.message + "' ) "; 

    def stringified ( self ): # used to later send the data to the frontend
        return '{ "id":' + str( self.id ) + ', "send_id":' + str( self.send_id ) + ', "get_id":' + str( self.get_id ) + ', "message":"' + self.message + '" } '; 


def get_users (): # get all the users of the database
    conn = MySQLdb.connect( "localhost", "root", "thedb" )
    crs = conn.cursor();

    # execute SQL query using execute() method.
    crs.execute( "SELECT * FROM dbase.users ORDER BY id ASC;" )
    users_tuples = crs.fetchall()

    users_data = []
    for i in users_tuples:
        users_data.extend( i )

    conn.close();

    users = [];
    for i in range( len( users_data ) ):
        if ( i + 6 >= len( users_data ) ):
            break;

        if ( i % 7 != 0 ):
            continue;

        users.append( User( users_data[ i ], users_data[ i + 1 ], users_data[ i + 2 ], users_data[ i + 3 ], users_data[ i + 4 ], users_data[ i + 5 ] , users_data[ i + 6 ] ) );

    return users

def get_talks (): # get all the talks of the database
    conn = MySQLdb.connect( "localhost", "root", "thedb" )
    crs = conn.cursor();

    # execute SQL query using execute() method.
    crs.execute( "SELECT * FROM dbase.talks ORDER BY id ASC;" )
    talks_tuples = crs.fetchall()

    talks_data = []
    for i in talks_tuples:
        talks_data.extend( i )

    conn.close();

    talks = [];
    for i in range( len( talks_data ) ):
        if ( i + 3 >= len( talks_data ) ):
            break;

        if ( i % 4 != 0 ):
            continue;

        talks.append( Talk( talks_data[ i ], talks_data[ i + 1 ], talks_data[ i + 2 ], talks_data[ i + 3 ] ) );

    return talks


def db_execute ( server, user, password, code ): # execute any code onto the database
    db_conn = MySQLdb.connect( server, user, password )
    db_result = db_conn.cursor()

    db_result.execute( code )

    # print(db_result.fetchall())

    db_conn.commit()
    db_conn.close()


def get_talk_id (): # get a new, unique id
    talks = get_talks();
    for i in range( len( talks ) - 1 ):
        if ( talks[ i + 1 ].id - talks[ i ].id > 1 ):
            return talks[ i ].id + 1;
    return len( talks )

@eel.expose
def get_send_talks_for_user ( id ): # returns all talks that the user sent
    talks = get_talks();
    user_talks = "[ ";
    for i in range( len( talks ) ):
        if ( talks[ i ].send_id == id ):
            if ( user_talks != "[ " ):
                user_talks = user_talks + ", ";
            user_talks = user_talks + talks[ i ].stringified();
    user_talks = user_talks + " ]";
    return user_talks

@eel.expose
def get_get_talks_for_user ( id ): # returns all talks that the user got
    talks = get_talks();
    user_talks = "[ ";
    for i in range( len( talks ) ):
        if ( talks[ i ].get_id == id ):
            if ( user_talks != "[ " ):
                user_talks = user_talks + ", ";
            user_talks = user_talks + talks[ i ].stringified();
    user_talks = user_talks + " ]";
    return user_talks

def get_all_talks_for_user ( id ): # returns all talks that the user got and sent
    talks = get_talks()
    user_talks = []
    for i in range( len( talks ) ):
        if ( talks[ i ].get_id == id ):
            # print("gets")
            user_talks.append(talks[i])
        if ( talks[ i ].send_id == id ):
            user_talks.append(talks[i])
    # print(user_talks)
    # print(talks)
    # print(id)
    return user_talks

@eel.expose
def add_talk ( send_id, get_id, message ): # adds a talk to the database
    command = 'INSERT INTO dbase.talks VALUES ( ' + str( get_talk_id() ) + ', ' + str( send_id ) + ', ' + str( get_id ) + ', "' + message + '" );'
    db_execute( "localhost", "root", "thedb", command );

@eel.expose
def delete_talk ( id ): # deletes a talk from the database
    command = 'DELETE FROM dbase.talks WHERE id=' + str( id ) + ";";
    db_execute( "localhost", "root", "thedb", command );






def get_user_id (): # get a new, unique id
    users = get_users();
    for i in range( len( users ) - 1 ):
        if ( users[ i + 1 ].id - users[ i ].id > 1 ):
            return users[ i ].id + 1;
    return len( users )
 
@eel.expose
def get_user ( username, password ): # log in the user usingn their username and password
    users = get_users();
    for i in range( len( users ) ):
        if ( users[i].username == username and users[i].password == password ):
            return [ users[i].id, users[i].username, users[i].password, users[i].fullname, users[i].age, users[i].is_admin, users[i].email ];
    return -1

@eel.expose
def get_user_just_though_username ( username ): # return user using only their unique username
    users = get_users();
    for i in range( len( users ) ):
        if ( users[i].username == username ):
            return [ users[i].id, users[i].username, users[i].password, users[i].fullname, users[i].age, users[i].is_admin, users[i].email ];
    return -1

@eel.expose
def get_user_just_though_id ( id ): # return user using only their unique id
    users = get_users();
    for i in range( len( users ) ):
        if ( users[i].id == id ):
            return [ users[i].id, users[i].username, users[i].password, users[i].fullname, users[i].age, users[i].is_admin, users[i].email ];
    return -1

@eel.expose
def add_user ( username, password, fullname, age, is_admin, email ): # add user to the database
    users = get_users();
    for i in range( len( users ) ):
        if ( users[i].username == username ):
            # eel.load( "signup.html" );
            return 0; # username taken choose another one
    id = get_user_id();
    command = 'INSERT INTO dbase.users VALUES ( ' + str( id ) + ', "' + str( username ) + '", "' + str( password ) + '", "' + str( fullname ) + '", ' + str( age ) + ', ' + str( is_admin ) + ', "' + str( email ) + '" );'
    # # print(command);
    db_execute( "localhost", "root", "thedb", command );

    return [ id, username, password, fullname, age, is_admin, email ]; # username available, user was added

@eel.expose
def update_user ( id, username, password, fullname, age, is_admin, email ): # edit the user, applying changes to the database
    command = 'UPDATE dbase.users SET username = "' + username + '", password = "' + password + '", fullname = "' + fullname + '", is_admin = ' + is_admin + ', email = "' + email + '" WHERE id = ' + str(id) + ';'
    db_execute( "localhost", "root", "thedb", command );


@eel.expose
def delete_user ( id ): # delete a user and their talks
    command1 = "DELETE FROM dbase.talks WHERE send_id=" + str( id ) + " OR get_id=" + str( id ) + ";";
    # print(command1)
    db_execute( "localhost", "root", "thedb", command1 );

    command2 = 'DELETE FROM dbase.users WHERE id=' + str( id ) + ';';
    db_execute( "localhost", "root", "thedb", command2 );




@eel.expose
def upload(): # used to upload data file for making charts
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    uploaded_file = filedialog.askopenfile()
    chart(read_file_to_variable(uploaded_file.name))








#  Done by Michal
#  function saving pdf
def save_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="EDINBURGH NAPIER UNIVERSITY EXERCISE THRESHOLDS APP", ln=1, align='C')
    pdf.image("web/chart1.png", x=5,   y=25, w=100, h=73)
    pdf.image("web/chart2.png", x=105, y=25, w=100, h=73)
    pdf.image("web/chart3.png", x=5,   y=119, w=100, h=73)
    pdf.image("web/chart4.png", x=105, y=119, w=100, h=73)
    pdf.image("web/chart5.png", x=5,   y=212, w=100, h=73)
    pdf.set_font("Arial", size=8)
    pdf.set_xy(16, 99)
    pdf.multi_cell(w=80, h=3, border=0, txt="The gas exchange threshold  is a useful measure of exercise tolerance when paired against how much oxygen and carbon dioxide intake occurs.")
    pdf.set_xy(116, 99)
    pdf.multi_cell(w=80, h=3, border=0, txt="Above is a ventilatory Equivalents for Oxygen (VE/VO2): refers to number of liters of. ventilation per liter of oxygen  consumed. The normal value is typically around. 25-30 and  increases once the person reaches their ventilatory threshold.")
    pdf.set_xy(16, 194)
    pdf.multi_cell(w=80, h=3, border=0, txt="VO2 max is the amount (volume) of oxygen your body uses while exercising as hard as you can.  Knowing your VO2 max can help you train for sports, track your fitness improvement, and improve your heart health.")
    pdf.set_xy(116, 194)
    pdf.multi_cell(w=80, h=3, border=0, txt="VO2 max by Work Rate (W)   ")
    pdf.set_xy(100, 260)
    pdf.multi_cell(w=70, h=3, border=0, txt="Seen above is  heart rate levels during exercise when calculated in beats per minute. The best way to increase your Vo2 max is to exercise near your maximum heart rate.")

    pdf.output("web/result.pdf")

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
    plt.savefig("web/chart1.png", dpi=120)

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
    plt.savefig("web/chart2.png", dpi=120)

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
    plt.savefig("web/chart3.png", dpi=120)

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
    plt.savefig("web/chart4.png", dpi=120)

    # drawing   Heart rate / Work Rate" graph
    fig, ax = plt.subplots()
    plt.scatter(wr, hr, alpha=0.8, s=40, linewidths=0.05)
    plt.title("Heart rate", fontsize=19, loc='left', y=1.02)
    plt.xlabel("Work Rate (W)", fontsize=14)
    plt.ylabel("Heart rate (Beats/ Min)", fontsize=14)
    # placing the Napier logo in right top corner
    plot_setup_insert_logo()
    # plt.show()
    plt.savefig("web/chart5.png", dpi=120)

    save_pdf();

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

eel.start( "index.html", mode="chrome-app" ) # start the eel application
