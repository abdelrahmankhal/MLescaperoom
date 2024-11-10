import numpy as np
data = np . array ([[2 , 4] , [4 , 6] , [5 , 9] , [7 , 10]])
labels = [ 'Normal' , 'Warning' , 'Maintenance Needed' , 'fault']
new_machine = np . array ([5 , 8])
distances = np . linalg . norm ( data - new_machine , axis =1)
# Find the index of the nearest neighbor
nearest_index = np.argmin(distances)
classification = labels [ nearest_index ]
print ( f" The new machine is classified as : {classification }")