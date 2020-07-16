import numpy as np
import random
from matplotlib import pyplot as plt
from .ant import Ant

class AntColonyOptimization:
  def __init__(self, population_size, tsp_map, q, evaporation_rate):
    self.population_size = population_size
    self.tsp_map = tsp_map
    self.distances = np.zeros((len(tsp_map), len(tsp_map)))
    for i in range(0, len(tsp_map)):
      for j in range(i+1, len(tsp_map)):
        self.distances[i,j] = ( (tsp_map[i][0] - tsp_map[j][0])**2 + (tsp_map[i][1] - tsp_map[j][1])**2 ) ** (1/2)
        self.distances[j,i] = self.distances[i][j]
    self.pheromones = np.ones((len(tsp_map), len(tsp_map))) * 0.000001
    self.q = q
    self.evaporation_rate = evaporation_rate
  
  def run(self, iterations):
    ants = []
    #Create ants
    for i in range(0, self.population_size):
      ants.append(Ant(self.distances, 1, 5))
    #Iterate from ants
    best_distance = float('Inf')
    best_path = []
    for i in range(0, iterations):
      delta_pheromones = np.zeros((len(self.pheromones), len(self.pheromones)))
      for ant in ants:
        path, distance = ant.run(random.randint(0, len(self.distances) - 1), self.pheromones)
        if distance < best_distance:
          best_distance = distance
          best_path = path
        #Update pheromones
        delta_value = self.q / distance
        for index in range(1, len(path)):
          delta_pheromones[path[index], path[index-1]] += delta_value
          delta_pheromones[path[index-1], path[index]] += delta_value
      elite_pheromones = np.zeros((len(self.pheromones), len(self.pheromones)))
      for index in range(1, len(best_path)):
          elite_pheromones[best_path[index], best_path[index-1]] += 5*delta_value
          elite_pheromones[best_path[index-1], best_path[index]] += 5*delta_value
      self.pheromones = ((1-self.evaporation_rate) * self.pheromones) + delta_pheromones + elite_pheromones
      print(i)
    best_run = []
    for node in best_path:
      best_run.append(self.tsp_map[node])
    best_run = np.array(best_run)
    print('best_distance', best_distance)
    plt.plot(best_run[:,0], best_run[:,1], marker="o", markersize=10)
    plt.show()