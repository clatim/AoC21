import numpy as np

# Read in the depths
depths = np.loadtxt("input1.txt", dtype='int')

ct = 0
# First entry has nothing to compare to, so initialise compare to 
# the first entry + 1 so it alway returns false
compare = depths[0]+1
for depth in depths:
  if depth > compare:
    ct = ct+1
  compare = depth

print (f'The number of deepers is: {ct}')


print (f'There is too much noise captain, we are going to the'
  f' sliding window!')

ct = 0
# This is equivalent to ii = 1
old = np.sum(depths[0:3])

for ii in range(2,depths.size-1):
  # PYTHON SLICES ARE INCLUSIVE AT ONE END AND NOT AT THE OTHER
  # WHHHHHHYYYYYYY
  new = np.sum(depths[ii-1:ii+2])
  if new > old:
    ct = ct+1
  old = new

print (f'The sliding method gave us this many deepers: {ct}')