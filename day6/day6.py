import numpy as np

# with open('test.txt','r') as f:

population = np.genfromtxt('input6.txt', dtype='int', delimiter=',')

day = 0
while day < 256:
  # print(f"after {day} day {population}")
  population = population-1
  new_fish = 0
  for fish in range(population.size):
    if population[fish] == -1:
      new_fish +=1
      population[fish] = 6
  # print(population)
  born = np.full(new_fish, 8)
  population = np.append(population, born)
  day += 1

print(f"After {day} days the population is {population.size}")