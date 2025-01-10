

"""

Filename: Basin_of_attraction_with_alpha_of_8.96_plot_using_data_file.py
Name: Khang Ly 
Date: Wednesday, 10th of October, 2024  
Project's Name: Plot using data text file (basin of attraction)
Description: 
    This script is to plot the basin of attraction from reading the 
    data text file that generated from the 'basin_of_attraction_of
    _Rulkov_Map' script to help save plotting time. This one is for alpha
    value of 8.96. 


"""

# Import necessary packages 


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# Access the data and read 

data = []
with open('basin_of_attraction_orbit_of_alpha_8_96_data_v.4.txt', 'r') as file:
    for line in file :
        # Remove parentheses and split by comma 
        data.append(eval(line.strip()))
        
# Convert to DataFrame 

df = pd.DataFrame(data, columns=['Index1', 'Index2', 'X', 'Y', 'Value', 'Color'])

# Explore the Data
print(df.head())

# Step 5: Plot the Data
plt.figure(figsize=(10, 6))

# Scatter plot with color 

plt.scatter(df['X'], df['Y'], c=df['Color'])
# Plot points and lines with marker size specified 
#marker_size = 3  # Adjust this value to change the size of the markers 
#for i in range(len(x_init)):
 #   plt.plot(x_values[:, i], y_values[:, i], marker='o', linestyle='-', label=f'Start: ({x_init[i]}, {y_init[i]})', color='yellow', markersize = marker_size)

# Add labels and title 

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of X vs Y with Color 500 x 500 grid with new epsilon values, bigger white box')

# Show the plot 

plt.show()
