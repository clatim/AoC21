import numpy as np

def get_neighbours(heights, x, y):
  neighbours = [heights[x,y+1],heights[x,y-1],heights[x-1,y],heights[x+1,y]]
  return [x for x in neighbours]

with open('input9.txt','r') as f:
  num_cols = len(f.readline().strip())
  f.seek(0)
  num_rows = sum(1 for line in f)

  # We add 2 to the sizes we found as we want neighbouring zeros
  # for easier programming
  heights = np.ones([num_rows+2,num_cols+2])
  # Initialise values to 10 as at the moment 9 is the highest value we read
  # from the input file. This stops us missing locals
  heights = heights*10

  # Put the heights into the np array offset by 1.
  f.seek(0)
  for ii, line in enumerate(f):
    for jj, height in enumerate(line.strip()):
      heights[ii+1,jj+1] = height

nines = [heights >= 9]
lowest_points = []
risk_level = 0
# now it is loaded see if the height is a local minimum
# I think this is the most efficient array access pattern in Python
for ii in range(1,num_rows+1):
  for jj in range(1,num_cols+1):
    # print( "checking", heights[ii,jj])
    if all(heights[ii,jj] < nei for nei in get_neighbours(heights,ii,jj)):
      risk_level += heights[ii,jj]+1
      lowest_points.append([ii,jj])
      print( f"Found local at {ii,jj,heights[ii,jj]}")
      # Lets find the basin sizes


print(f"The risk level is {int(risk_level)}")

print(lowest_points)




