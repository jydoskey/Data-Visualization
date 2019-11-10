import matplotlib.pyplot as plt

#Define the values to be used
x_cube = [1, 2, 3, 4, 5]
y_cube = [1, 8, 27, 64, 125]

#Make the plot
plt.plot(x_cube, y_cube, linewidth=4)

#Labelling of the axis
plt.title('Cube Plot of first 5 Numbers', fontsize='14')
plt.xlabel('First 5 Numbers', fontsize='10')
plt.ylabel('Cube of First 5 Numbers', fontsize='10')

#plt.tick_params(axis='both', labelsize='10')

#Show the plot
#plt.show()

#Save the plot
plt.savefig('First 5 Numbers cube_plot', bbox_inches='tight')