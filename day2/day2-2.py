import numpy as np

with open('input2.txt', 'r') as f:
  commands = f.readlines()
  depth, horizontal, aim = 0, 0, 0
  for command in commands:
    where, magnitude = command.split()
    magnitude = np.int(magnitude)
    if where == 'forward': 
      horizontal += magnitude
      depth += aim*magnitude
    elif where == 'down':
      aim += magnitude
    elif where == 'up':
      aim -= magnitude
    else:
      print (f"So what direction is {where} then? HUH?!")


print (f"Product of depth and horizontal position (including aim) is: {depth*horizontal}")
    
