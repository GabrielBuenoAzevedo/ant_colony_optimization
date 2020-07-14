from matplotlib import pyplot as plt
from classes.ant import Ant
import numpy as np

#Open input file
file = open('./dataset/berlin52.tsp')

#Read header files
name = file.readline()
file_type = file.readline()
comment = file.readline()
dimension = file.readline()
edge_weight_type = file.readline()
file.readline()

#Get cities coordinates
cities = []
for line in file:
  if line == 'EOF\n' or line == ' ':
    break
  line_info = line.split(' ')
  cities.append( [ float(line_info[1]), float(line_info[2])] )
cities = np.array(cities)

cities = np.array([
  [1,1],[1,2],[2,3],[3,2],[3,1]
])

#Print graph
# plt.scatter(cities[:,0], cities[:,1], marker="o", s=10)
# plt.show()

#Get distance from each city (d(i,j) equals to d(j,i))
distances = np.zeros((len(cities), len(cities)))
for i in range(0, len(cities)):
  for j in range(i+1, len(cities)):
    distances[i,j] = ( (cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2 ) ** (1/2)
    distances[j,i] = distances[i][j]

# print(distances)
ant = Ant(distances, 1, 1)

pheromones = np.ones((len(cities), len(cities))) * 0.001
path = ant.run(1, pheromones)

best_run = []
for node in path:
  best_run.append(cities[node])
best_run.append(cities[1])

best_run = np.array(best_run)
plt.plot(best_run[:,0], best_run[:,1], marker="o", markersize=10)
plt.show()