# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import psycopg2 as pg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import datetime as dt

 
# Connect to your postgres DB
conn = pg.connect("dbname=postgres user=postgres password=admin")

# Open a cursor to perform database operations
cur = conn.cursor()

#Create t_stamp parameters for query
start_stamp = '2023-03-03 13:23:13.426'
t_stamp_conv = dt.datetime.strptime(str(start_stamp), '%Y-%m-%d %H:%M:%S.%f') 
end_stamp = t_stamp_conv + dt.timedelta(seconds = 5)

# Execute a query
cur.execute("""SELECT * 
                FROM (SELECT "Time_Stamp", "Robot_Name", "Torque_1", "Amp_1"  
                      FROM everything 
                      WHERE "Robot_Name" = 'denso_01' and "Time_Stamp" > (%s) and "Time_Stamp" < (%s)
                      ORDER BY "Time_Stamp" DESC 
                      LIMIT 300) as live_data
                ORDER BY "Time_Stamp" ASC
                """, (start_stamp, end_stamp,))
                
colnames = [desc[0] for desc in cur.description]

# Retrieve query results
records = cur.fetchall()

#Convert to Pandas Dataframe for Processing
data = pd.DataFrame(data = records, columns = colnames)





# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# Initialize communication with TMP102
#tmp102.init()

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
    #temp_c = round(tmp102.read_temp(), 2)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()




