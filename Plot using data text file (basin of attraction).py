
"""

Filename: Plot_using_data_txt_file_(basin_of_attraction)
Name: Khang Ly 
Date: Wednesday, 10th of July, 2024  
Project's Name: Plot using data text file (basin of attraction)
Description: This script is to plot the basin of attraction from reading the 
            data text file that generated from the 'basin_of_attraction_of
            _Rulkov_Map' script to help save plotting time. 


"""

# Import necessary packages 

import pandas as pd 
import matplotlib.pyplot as plt 

# Access the data and read 

data = []
with open('basin_of_attraction_data.txt', 'r') as file:
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

# Add labels and title 

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of X vs Y with Color 4000 x 4000 grid')

# Show the plot 

plt.show()
