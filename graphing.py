import pandas as pd
# load dataset as a data frame
results = pd.read_csv('frame.csv')

# select relevant columns
data = results[['order_size', 'reorder_point', 'total_cost']]

# for each combination of order size and reorder point, compute average response
data = data.groupby(['reorder_point', 'order_size']).mean()

# reset data index and rename columns
data.reset_index(inplace = True)
data.columns = ['reorder_point', 'order_size', 'cost']

# pivot dataset
data = data.pivot('reorder_point', 'order_size')

# map values
import numpy as np



X = data.columns.levels[1].values  # order sizes
Y = data.index.values # reorder points
Z = data.values # average total cost
Xi, Yi = np.meshgrid(X,Y)

import optim

# run the algorithm with 3 different starting points
a = optim.LocalSearch([90,90], 20, 8)
b = optim.LocalSearch([90,10], 20, 8)
c = optim.LocalSearch([20,80], 20, 8)

print(a.path)

import matplotlib as plt

# re-create contour plot
plt.figure(dpi=125)
plt.title('Contour plot for simulation model')
plt.xlabel('Reorder point')
plt.ylabel('Order size')
contours = plt.contour(Yi, Xi, Z, 10)
plt.clabel(contours, inline=True, fmt='%1.0f', fontsize=8)
plt.grid(color='gray', linestyle='-', linewidth=.15)

# add lines to visualize algorithms path
plt.plot(a.path[:,0],a.path[:,1],'b-o')
plt.plot(b.path[:,0],b.path[:,1],'g-o')
plt.plot(c.path[:,0],c.path[:,1],'r-o')
plt.show()