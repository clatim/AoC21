import numpy as np
from scipy.optimize import minimize

def fuel_cost_part1(p, x):
  """ 
  Calculates the cost in fuel to move all crabs from
  their position in x to p

  The cost to move a crab is the difference between where it starts
  and where it ends, so is abs(x-p).

  Therefore, all we need to do is sum over the number of crabs.
  """
  return sum([np.abs(val - p) for val in x])

def fuel_cost_part2(p, x):
  """ 
  Calculates the cost in fuel to move all crabs from
  their position in x to p for part 2

  Let m how far a crab must move, then the cost to move a crab m places
  is sum( [val+1 for val in range(m)]). However, this is only valid for integers
  so we need something to approximate it that is differentiable so that minimise works.

  Turns out we can approximate this above behaviour for real numbers by saying:
  the cost to move a crab m places is m*(m+1)*0.5.
  We do that here.

  Then, all we need to do is sum over the number of crabs.
  """
  fuel_cost = 0
  for val in x:
    to_move = np.abs(val-p)
    fuel_cost += to_move*(to_move+1)*0.5

  return fuel_cost

def move_cost(p):
  return sum( [ np.abs(p-x) for x in range(int(np.floor(p))) ] )

x = np.genfromtxt('input7.txt',dtype='int',delimiter=',')

min_fuel = minimize(fuel_cost_part1, 0, args=x)
print (f"The minimum fuel is {int(min_fuel.fun)}")

min_fuel = minimize(fuel_cost_part2, 0, args=x)
# Note, we need to restrict to an integer solution here. The problem is linear
# so the nearest integer will be the integer solution
print (f"The minimum fuel for part 2 {int(fuel_cost_part2(np.rint(min_fuel.x),x))}")
