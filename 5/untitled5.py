data = [3.1 , 2.9 , 5.4 , 6.2 , 1.9 , 5.7]
threshold = 3.5
cluster_1 = [ x for x in data if x <=3.5]
cluster_2 = [ x for x in data if x > 3.5]
print ( f" Cluster 1: { cluster_1 }")
print ( f" Cluster 2: { cluster_2 }")