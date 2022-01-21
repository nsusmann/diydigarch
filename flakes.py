# This script was altered in January 2022 for the purposes of teaching an introductory coding lesson to undergraduate archaeology students. 
# This script was originally created by Chloe Holden in 2020. Her work is available here: https://blogs.iu.edu/sciu/2020/01/18/archaeology-and-python/
# Use this version of the script to load in rep.lit. Begin by pasting this script in main.py. Search for pip in the install packages tab and install it.

import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as pip

# Import excel files with the X and Y coordinates for flake distributions
# x and y coordinates were created in QGIS and exported into an excel file
r_basalt = pd.ExcelFile("Basalt-Right.xlsx")  # x and y coordinates for flakes knapped by a right hander
l_basalt = pd.ExcelFile("Basalt-Left.xlsx")  # x and y coordinates for flakes knapped by a left hander
#Creating dataframes for Sheet 1 in left and right hander flake coordinates
df_right = r_basalt.parse("Sheet1")
df_left = l_basalt.parse ("Sheet1")
#Identifying individual X and Y columns and turning them into lists
#Right
right_x = df_right["x"].tolist()
right_y = df_right["y"].tolist()
#Left
left_x = df_left["x"].tolist()
left_y = df_left["y"].tolist()
# Create empty grid
S = 200 #dimension of grid, 200 square centimeters
N = 10 #dimension of the grid lines, 10 centimeters apart
#min and max from nail coordinates recorded by the total station
x_max = 101.517
x_min = 98.761
y_max = 100.000
y_min = 97.798
# Right Hander Plot
plt.hist2d(right_x, right_y, bins=S)
plt.colorbar()
plt.xlabel("x (meters)")
plt.ylabel("y (meters)")
plt.title("Right-Hander Flakes")
plt.savefig("rh.jpeg")
#clear the plot so as not to retain the color ramp on next graph
plt.clf()
# Left Hander Plot
plt.hist2d(left_x, left_y, bins=S)
plt.colorbar()
plt.xlabel("x (meters)")
plt.ylabel("y (meters)")
plt.title("Left-Hander Flakes")
plt.savefig("lh.jpeg")
