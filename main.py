from classes.antColonyOptimization import AntColonyOptimization
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

aco = AntColonyOptimization(len(cities), cities, 100, 0.5)
aco.run(500)