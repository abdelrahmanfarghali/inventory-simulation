import model as mdl
import numpy as np
import pandas as pd

max_packages = 6
inventories = 12
package_size = 45
order_sizes = np.random.randint(max_packages, size=(max_packages*inventories))
minimum_individual = 6
maximum_individual = 60
orders = np.random.randint(package_size - np.random.uniform(minimum_individual, maximum_individual), size=order_sizes[:32])
reorder_points = orders

length = 13.
num_replications = 15

help(mdl.run_experiments)
"""Args:
        - length: length of the simulation, in months
        - reorder_points: list of reorder points parameters to simulate 
        - order_sizes:list of order size parameters to simulate
        - num_rep: number of replications to run for each design point
        """

frame = pd.DataFrame(mdl.run_experiments(reorder_points, order_sizes, num_replications))
frame.to_csv('frame.csv')