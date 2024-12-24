
"""

Name: Khang Ly 
Tuesday, July 1st, 2024
Basin of Attraction of Rulkov Map (final version)

"""

# Import all the necessary modules 

import time
import numpy as np
import matplotlib.pyplot as plt 
from tqdm import tqdm 
from datetime import datetime

# Define a function to clear the data file

def clear_data_file(filename):
    with open(filename, 'w') as file:
        file.truncate()
        
# Define the filename 
filename = 'basin_of_attraction_data.txt'

# Clear the previous data in the file
clear_data_file(filename)

# Create a header in the txt file 

def write_header_to_file(filename, script_name, description, author, date):
    header = f"""
    =====================================
Script Name: {script_name}
Description: {description}
Author: {author}
Date: {date}
Paramaters: 
    a = 25.0375
    o = -4.38
    u = 0.25 
=====================================
    """
    with open(filename, 'w') as file:
        file.write(header.strip() + "\n")

# Example usage
def main():
    script_name = 'basin_of_attraction_of_Rulkov_Map.py'
    description = "Examining the basin of attraction of the Rulkov Map, with two states: Equilibrium (where is converge to the equilibrium point) and other states (e.g.Loop), with the given parameters"
    author = 'Khang Ly'
    date = datetime.now()

    write_header_to_file(filename, script_name, description, author, date)

if __name__ == "__main__":
    main()


# Constant variables 

a = 25.0375 
o = -4.38
u = 0.25 

epsilon = 1e-8
xp = -5.379999999999999     # Equilibrium point of x-coordinate
yp = -9.30437304075235      # Equilibrium point in y-coordinate
xmin = xp - epsilon 
xmax = xp + epsilon 
ymin = yp - epsilon 
ymax = yp + epsilon 

nmax = 2000 

min_x = float(input("Enter the minimum domain: "))
max_x = float(input("Enter the maximum domain: "))
min_y = float(input("Enter the minimum range: "))
max_y = float(input("Enter the maximum range: "))

x_range = (min_x, max_x)
y_range = (min_y, max_y)

# Define the number of segments in each axis 

num_segments_x = int(input("Enter the number of segment for x: "))
num_segments_y = int(input("Enter the number of segment for y: "))

# Start timing the script

start_time = time.time()

# Create the X and Y array 

xgrid = np.zeros(num_segments_x)
ygrid = np.zeros(num_segments_y)
basin = np.zeros((num_segments_x,num_segments_y))

# Calculate the step size for each segment 

x_step = (x_range[1] - x_range[0]) / num_segments_x
y_step = (y_range[1] - y_range[0]) / num_segments_y



# Define a function to represent f(x,y)

def nonlinear_function(a,xi,yi):
     if xi <= 0:
         return (a / (1-xi)) + yi
     elif xi < (a+yi):
         return (a+yi)
     else:
         return -1 

# Create x and y grid 

for i in range(num_segments_x):
    xi = x_range[0] + (i + 0.5) * x_step
    xgrid[i] = xi 
for j in range(num_segments_y):
    yi = y_range[0] + (j + 0.5) * y_step
    ygrid[j] = yi 
    

for i in tqdm(range(num_segments_x), desc="Processing x segments"):
    center_x = x_range[0] + (i + 0.5) * x_step
    xi = center_x   
    for j in range(num_segments_y):
        center_y = y_range[0] + (j + 0.5) * y_step
        yi = center_y
        #print(i,j)
        
# Create a for loop to get rid of the transient 

        for n in range(2000):
           #print(n,xi,yi)
           x1 = nonlinear_function(a, xi, yi)
           y1 = yi - u*(xi+1) + (u*o)

           x = x1
           y = y1 
           
# Create a while loop to get rid of the transient 

        n = 1
        while n <= nmax:
            x1 = nonlinear_function(a, x, y)
            y1 = y - u*(x+1) + (u*o)
            
            if xmin < x < xmax and ymin < y < ymax:
               basin[i][j] = 1     # We are in the box so set the flag to 1 
               n == nmax + 1  # The condition that exit the loop 
    
            x = x1
            y = y1
            
            n += 1
            
# Save the data into a txt file

        coordinate = list(zip([i],[j],[xi],[yi],[basin[i][j]],['red' if basin[i][j] == 1.0 else 'blue']))
        for element in coordinate:
            file1 = open("basin_of_attraction_data.txt","a")
            file1.write(f"{element} \n")
            file1.close()

# Optimize plotting 

plt.ioff()

# Start timing the plotting process 

plot_start_time = time.time()

# Create a figure and axis object

fig, ax = plt.subplots()

# Plot the grid points with colors based on the basin array

for i in tqdm(range(num_segments_x)):
    for j in range(num_segments_y):
        color = 'red' if basin[i][j] == 1 else 'blue'
        ax.scatter(xgrid[i], ygrid[j], c=color)

# Set labels and title

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(f'Basin of Attraction\nSegments: {num_segments_x} x {num_segments_y}')

# Create legend outside the graph

blue_patch = plt.Line2D([0], [0], marker='o', color='blue', label='Other states')
red_patch = plt.Line2D([0], [0], marker='o', color='red', label='Equilibrium')
plt.legend(handles=[blue_patch, red_patch], loc='center left', bbox_to_anchor=(1, 0.5))

# Display the plot 

plt.show()

# End plot timing 

plot_end_time = time.time()

plt.ion()

# Calculate and print the runtime 

plot_runtime = plot_end_time - plot_start_time
hours, remainder = divmod(plot_runtime, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"Plotting time: {int(hours):02}:{int(minutes):02}:{seconds:06.3f}")

# End timing the script

end_time = time.time()

print(f"Start Time: {time.ctime(start_time)}")
print(f"End Time: {time.ctime(end_time)}")

# Calculate and print the runtime

runtime = end_time - start_time
hours, remainder = divmod(runtime, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"Script runtime: {int(hours):02}:{int(minutes):02}:{seconds:06.3f}")





