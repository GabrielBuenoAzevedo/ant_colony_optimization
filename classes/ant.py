import numpy as np
import copy
import random

class Ant:
  def __init__(self, tsp_map, alpha, beta):
    self.map = tsp_map
    self.visited_cities = []
    self.path_length = 0
    self.alpha = alpha
    self.beta = beta
    
  def run(self, initial_pos, pheromones):
    #Deep copy all info on the map and pheromones map
    tsp_map = copy.deepcopy(self.map)
    pheromones = copy.deepcopy(pheromones)
    #Starts in the initial position
    available_cities = np.arange(len(tsp_map))
    current_pos = initial_pos
    path = [initial_pos]
    available_cities = available_cities[ available_cities != current_pos ]
    while len(available_cities) > 0:
      curr_line = tsp_map[current_pos]
      #do things
      new_pos = self.chooseNextCity(available_cities, current_pos, curr_line, pheromones)
      tsp_map[:,current_pos] = 0
      tsp_map[current_pos,:] = 0
      current_pos = new_pos
      path.append(current_pos)
      available_cities = available_cities[ available_cities != current_pos ]
      print('\n-----------------------------------------------------------\n')
    print('--------------------------------\nPath: ', path)
    return path
  
  def chooseNextCity(self, available_cities, curr_pos, curr_distances, pheromones):
    curr_distances = [ (1/distance) ** self.beta if distance > 0 else 0 for distance in curr_distances]
    pheromones = pheromones[curr_pos] ** self.alpha
    values = curr_distances * pheromones
    probabilities = values / sum(values)
    cumulative_probability = 0
    random_choice = random.random()
    print('probabilities: ', probabilities)
    print('random_choice: ', random_choice)
    for (index,probability) in enumerate(probabilities):
      cumulative_probability += probability
      if random_choice < cumulative_probability:
        return index
    # return random.choice(available_cities)
