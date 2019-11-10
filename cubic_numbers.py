import matplotlib.pyplot as plt

#Definition of values
x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]

#Plot the x and y values
plt.scatter(x_values, y_values, cmap=plt.cm.Greens, c=y_values, edgecolor='none', s=40)

#Axis labelling
plt.title('Cube plot of 1 to 5000', fontsize='16')
plt.xlabel('1 to 5000', fontsize='10')
plt.ylabel('cube of 1 to 5000', fontsize='10')

plt.axis([0, 5000, 0, 125000000000])


plt.show('Normal plot of 1 to 5000 against cube_colormap')


