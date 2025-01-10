
"""

Filename: Basin_of_attraction_(data_without_plotting)
Name: Khang Ly 
Tuesday, July 1st, 2024
Description:
    This script will print out the final states of the each initial conditions 
    onto a txt files that will get access later to plot out the basin of attraction. 

"""

# Import all the necessary modules 

import time
import numpy as np
from tqdm import tqdm 

# Define a function to clear the data file

def clear_data_file(filename):
    with open(filename, 'w') as file:
        file.truncate()
        
# Define the filename 
filename = 'basin_of_attraction_data.txt'

# Clear the previous data in the file
clear_data_file(filename)

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