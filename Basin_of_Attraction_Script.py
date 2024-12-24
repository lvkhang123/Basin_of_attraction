
"""

Filename: Plot_the_basin_of_attraction.py
Name: Khang Ly
Date: May 20th, 2024
Description:
    Plot the basin of attraction with the given parameters, ranges, and resolution 
        Red circles = Approach equilibrium points 
        Blue circles = Approach different states 

"""

import matplotlib.pyplot as plt 

# Set the value of parameters alpha (a), sigma (o), and meu (u)

a = 25.0375
o = -4.38
u = 0.25 

epsilon = 10e-8
xp = -5.379999999999999
yp = -9.30437304075235
xmin = xp - epsilon 
xmax = xp + epsilon 
ymin = yp - epsilon 
ymax = yp + epsilon 


# Create the X and Y array 

X = []
Y = []

# Define the range for the x and y axes 
x_range = (-25.0, 20.0)
y_range = (-25.0, 0.0)

# Define the number of segments in each axis 
num_segments_x = 10
num_segments_y = 10

# Calculate the step size for each segment
x_step = (x_range[1] - x_range[0]) / num_segments_x
y_step = (y_range[1] - y_range[0]) / num_segments_y

# Create a figure and axis object
fig, ax = plt.subplots(1,1, figsize=(16,9))
#ax.plot(X,Y)

# Increase the size of tick labels on both x and y axes
plt.xticks(fontsize=25)  # Adjust the fontsize as needed
plt.yticks(fontsize=25)  # Adjust the fontsize as needed

# Adding labels and title
plt.xlabel('x', fontsize=25)  # Adjust the fontsize as needed
plt.ylabel('y', fontsize=25)  # Adjust the fontsize as needed
plt.title('Basin of attraction of a 10 x 10 resolution', fontsize=30)  # Adjust the fontsize as needed

plt.legend(fontsize = 25) # Adjust the fontsize as needed 
'''
# Set the x and y limits
ax.set_xlim(x_range)
ax.set_ylim(y_range)

# Draw x and y axes lines
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Set aspect ratio to be equal to avoid distortion
ax.set_aspect('equal', 'box')

# Label the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Add a grid
ax.grid(True, which='both')
'''
# Plot the center points of each segment
for i in range(num_segments_x):
    for j in range(num_segments_y):
        center_x = x_range[0] + (i + 0.5) * x_step
        center_y = y_range[0] + (j + 0.5) * y_step
       # ax.plot(center_x, center_y, 'ko')  # 'bo' stands for blue circle, you can customize the marker style and color
        
        xi = center_x    # Every x-value of every center points will become the x-value of the initial condition 
        yi = center_y    # Every y-value of every center points will become the y-value of the initial condition
        
# Define a function to represent f(x,y)

        def nonlinear_function(a,xi,yi):
            if xi <= 0:
                return (a / (1-xi)) + yi
            elif xi < (a+yi):
                return (a+yi)
            else:
                return -1 
    
# Create a for loop to get rid of the transient 

        for n in range(20000):
            print(n,xi,yi)
            x1 = nonlinear_function(a, xi, yi)
            y1 = yi - u*(xi+1) + (u*o)
    
            x = x1
            y = y1 

        for n in range(2000):
            print(n,x,y)
            x1 = nonlinear_function(a, x, y)
            y1 = y - u*(x+1) + (u*o)
        
            if xmin < x < xmax and ymin < y < ymax:
                ax.plot(xi, yi, 'ro',label='Equilibrium State')  # 'bo' stands for blue circle, you can customize the marker style and color
            else:
                ax.plot(xi, yi, 'bo',label='Other states')
        
            X.append(x1)
            Y.append(y1)
    
            x = x1
            y = y1 
    

            
# Plot

#fig, (ax1) = plt.subplots(1, 1, figsize=(16, 9)) 
#ax1.plot(X,Y)


'''
Notes:
    
    * Using while loops to fix the plotting 
    * After certain iteration, we need to stop the loop. 
    * Change the name of the x and y initial conditions, since we encounter an issue that 
        the point we are plotting is not the initial points but the equilibrium point. 
    * Should move the for loop into the big loop. In other words, move the for loop into a bigger loop
    
'''

# The next thing I will do is to figure out the while loop
