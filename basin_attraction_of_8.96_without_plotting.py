
"""

Filename: Basin_of_attraction_of_alpha_8.96_generate_data_file.py
Name: Khang Ly 
Day and Date: Thursday, 10th of October, 2024 
Description:
    This script is for plotting the basin of attraction of Rulkov map with parameters as follow: alpha = 8.96,
    sigma = 1, and meu equal 0.25.     

"""

# Import all the necessary modules 

import time
import numpy as np


# Define a function to clear the data file

def clear_data_file(filename):
    with open(filename, 'w') as file:
        file.truncate()
        
# Define the filename 
filename = 'basin_of_attraction_orbit_of_alpha_8_96_data_v.4.txt'

# Clear the previous data in the file
clear_data_file(filename)

# Constant variables 

a = 8.96
o = 1
u = 0.25 

# Epsilon way 1:
epsilon1 = 0.05 # (dimension for box around white point)
epsilon2 = 0.125 # (length dimension for rectangle around red point)
epsilon3 = 0.011 # (width diemsnion for rectangle around red point)

xw = 2.4377624
yw = -4.44608898    
xr = 3.36219491
yr = -4.34725998

xwmin = xw - epsilon1
xwmax = xw + epsilon1 
ywmin = yw - epsilon1 
ywmax = yw + epsilon1 

xrmin = xr - epsilon2 
xrmax = xr + epsilon2 
yrmin = yr - epsilon3 
yrmax = yr + epsilon3 

nmax = 2000 

min_x = -4
max_x = 7
min_y = -6.5
max_y = -2.5

x_range = (min_x, max_x)
y_range = (min_y, max_y)

# Define the number of segments in each axis 

num_segments_x = 10
num_segments_y = 10

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
    

for i in range(num_segments_x):
    center_x = x_range[0] + (i + 0.5) * x_step
    #xi = center_x 
    xi = xgrid[i]
    print(center_x - xgrid[i])
    print(i)
    for j in range(num_segments_y):
        center_y = y_range[0] + (j + 0.5) * y_step
        #yi = center_y
        yi = ygrid[j]
        print(center_y - ygrid[j])
        #print(i,j)
        
# Create a for loop to get rid of the transient 
        x = xi
        y = yi
        for n in range(200000):
           #print(n,xi,yi)
           x1 = nonlinear_function(a, x, y)
           y1 = y - u*(x+1) + (u*o)

           x = x1
           y = y1 
           
# Create a while loop to get rid of the transient 

        n = 1
        while n <= nmax:
            x1 = nonlinear_function(a, x, y)
            y1 = y - u*(x+1) + (u*o)
            
            x = x1
            y = y1
            
            if (x > xwmin) and (x < xwmax) and (y > ywmin) and (y < ywmax):
                basin[i][j] = 1     # We are in the box so set the flag to 1 
                n = nmax + 13  # The condition that exit the loop 
            if (x > xrmin) and (x < xrmax) and (y > yrmin) and (y < yrmax): 
                basin[i][j] = 2 
                n = nmax + 13 
            
            n += 1
 
        #print(basin[i][j], xi, yi, n, x, y)
       
            
# Save the data into a txt file

        coordinate = list(zip([i],[j],[xi],[yi],[basin[i][j]],['white' if basin[i][j] == 1.0 else ('red' if basin[i][j] == 2.0 else 'blue')]))
        if basin[i][j] == 0:
            print(xi,yi,n,x,y)
        for element in coordinate:
            file1 = open("basin_of_attraction_orbit_of_alpha_8_96_data_v.4.txt","a")
            file1.write(f"{element} \n")
            file1.close()

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.2f} seconds")
























