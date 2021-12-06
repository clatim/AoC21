import numpy as np
import re

with open("input5.txt",'r') as f:
  num_lines = sum(1 for line in f)
  # assemble the coordinates. We will check for straight lines later
  ords = [np.zeros((num_lines,2)), np.zeros((num_lines,2))]
  f.seek(0)
  for ii, line in enumerate(f):
    coords = [int(s) for s in re.findall(r'\d+', line)]
    # ords[0][ii,:] = np.min([coords[0],coords[2]]),np.max([coords[0],coords[2]])
    # ords[1][ii,:] = np.min([coords[1],coords[3]]),np.max([coords[1],coords[3]])
    ords[0][ii,:] = coords[0],coords[2]
    ords[1][ii,:] = coords[1],coords[3]

ords[0] = ords[0].astype('int')
ords[1] = ords[1].astype('int')
# Find max value in ords to find the size of the map
map = np.zeros((np.max(ords[0])+1,np.max(ords[1])+1))
diagonals = True

for ii in range(num_lines):
  x1 = ords[0][ii,0]
  x2 = ords[0][ii,1]
  y1 = ords[1][ii,0]
  y2 = ords[1][ii,1]
  if x1 == x2:
    map[x1 , np.min(ords[1][ii,:]):np.max(ords[1][ii,:])+1] += 1 
  if y1 == y2:
    map[np.min(ords[0][ii,:]):np.max(ords[0][ii,:])+1 , y1] += 1 

  # find if a line is diagonal with gradient 1 or -1
  gradient = (y2-y1)/(x2-x1)
  if np.abs(gradient) == 1 and diagonals:
    gradient = gradient.astype('int')
    # Gradient is 1 so length is abs(y2-y1) = abs(x2-x1)
    length = np.abs(y2-y1)
    for jj in range(0,length+1):
      # print(f"Adding to ({x1+np.sign(x2-x1)*jj},{y1+np.sign(y2-y1)*jj})")
      map[x1+np.sign(x2-x1)*jj,y1+np.sign(y2-y1)*jj] += 1
        
# print( map.transpose() )
print(f"There are {map[map>=2].size} intersections cap'n!")