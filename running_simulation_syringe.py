import model as mdl
import numpy as np
import pandas as pd

max_packages = 20
package_size = 1

#max_packages = 5
#package_size = 48

#max_packages = 5
#package_size = 300

inventories = 12
order_sizes = np.random.randint(max_packages, size=(max_packages*inventories))

if package_size > 1:
        orders = np.random.randint(package_size - np.random.uniform(package_size / 3, package_size), size=(max_packages*inventories))
elif package_size == 1:
        orders = np.random.randint(max_packages, size=(max_packages*inventories//6))

reorder_points = orders - order_sizes[:len(orders)]

length = 13.
num_replications = 5

help(mdl.run_experiments)
"""Args:
        - length: length of the simulation, in months
        - reorder_points: list of reorder points parameters to simulate 
        - order_sizes:list of order size parameters to simulate
        - num_rep: number of replications to run for each design point
        """

frame = pd.DataFrame(mdl.run_experiments(reorder_points, order_sizes, num_replications))
frame.to_csv('frame.csv')