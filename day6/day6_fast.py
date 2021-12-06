import numpy as np

# read in initial population
population = np.genfromtxt('input6.txt', dtype='int', delimiter=',')
# use a dict that has entries [-1,8] and whose values are the number
# of lantern fish with that long left until they give birth
pop_vals = dict([(ii,0) for ii in range(-1,9)])

for fish in population:
  pop_vals[fish] += 1

day = 0
while day < 256:
  for ii in range(9):
    pop_vals[ii-1] = pop_vals[ii]
  
  pop_vals[8] = pop_vals[-1]
  pop_vals[6] += pop_vals[-1]
  pop_vals[-1] = 0
  day += 1

print(f"After {day} days the population is {sum(pop_vals.values())}")