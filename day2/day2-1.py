import numpy as np

with open('input2.txt', 'r') as f:
  commands = f.readlines()

  depth = 0
  horizontal = 0
  for command in commands:
    where, magnitude = command.split()
    magnitude = np.int(magnitude)
    # Try it with pattern matching from Python3.10
    # match command.split():
    #   case["forward", num]:
    #     horizontal = horizontal + num
    #   case _:
    #     print (f"I don't know what {command} means")
    if where == 'forward': 
      horizontal = horizontal + magnitude
    elif where == 'down':
      depth = depth + magnitude
    elif where == 'up':
      depth = depth - magnitude
    else:
      print (f"So what direction is {where} then? HUH?!")


print (f"Product of depth and horizontal position is: {depth*horizontal}")
    
