import numpy as np

with open('input2.txt', 'r') as f:
  commands = f.readlines()

  depth = 0
  horizontal = 0
  aim = 0
  for command in commands:
    where, magnitude = command.split()
    magnitude = np.int(magnitude)
    if where == 'forward': 
      horizontal = horizontal + magnitude
      depth = depth + aim*magnitude
    elif where == 'down':
      aim = aim + magnitude
    elif where == 'up':
      aim = aim - magnitude
    else:
      print (f"So what direction is {where} then? HUH?!")


print (f"Product of depth and horizontal position (including aim) is: {depth*horizontal}")
    
