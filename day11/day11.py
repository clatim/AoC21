import numpy as np

with open('input11.txt','r') as f:
  num_lines = sum(1 for line in f)
  f.seek(0)
  line = f.readline()
  line_length = len(line.strip())
  print(f"There are {num_lines} lines with length {line_length}")
  octs_ori = np.zeros((line_length,num_lines))
  f.seek(0)
  for jj, line in enumerate(f):
    for ii, val in enumerate(line.strip()):
      octs_ori[ii,jj] = int(val)

print(octs_ori.transpose())
octs = np.copy(octs_ori)

flash_ct = 0
num_steps = 100
for step in range(num_steps):
  octs += 1
  flashed = []
  
  while np.any(octs > 9):
    for jj, row in enumerate(octs):
      for ii, col in enumerate(row):
        if octs[ii,jj] > 9:
          flashed.append((ii,jj))
          flash_ct += 1
          octs[ii,jj] = 0

          if ii > 0:
            octs[ii-1,jj] += 1
            if jj < octs.shape[1]-1:
              octs[ii-1,jj+1] += 1
            if jj > 0:
              octs[ii-1,jj-1] += 1

          if jj < octs.shape[1]-1:
            octs[ii,jj+1] += 1
          if jj > 0:
            octs[ii,jj-1] += 1

          if ii < octs.shape[0]-1:
            octs[ii+1,jj] += 1
            if jj < octs.shape[1]-1:
              octs[ii+1,jj+1] += 1
            if jj > 0:
              octs[ii+1,jj-1] += 1
  
  for me in flashed:
    octs[me[0],me[1]] = 0
  # print(octs)

print(f"After {num_steps} there has been {flash_ct} flashes.")

octs = octs_ori
print(octs_ori.transpose())
step = 0
flash_ct = 0
while not np.all(octs == 0):
  step += 1
  octs += 1
  flashed = []
  while np.any(octs > 9):
    for jj, row in enumerate(octs):
      for ii, col in enumerate(row):
        if octs[ii,jj] > 9:
          flashed.append((ii,jj))
          flash_ct += 1
          octs[ii,jj] = 0
          
          if ii > 0:
            octs[ii-1,jj] += 1
            if jj < octs.shape[1]-1:
              octs[ii-1,jj+1] += 1
            if jj > 0:
              octs[ii-1,jj-1] += 1

          if jj < octs.shape[1]-1:
            octs[ii,jj+1] += 1
          if jj > 0:
            octs[ii,jj-1] += 1

          if ii < octs.shape[0]-1:
            octs[ii+1,jj] += 1
            if jj < octs.shape[1]-1:
              octs[ii+1,jj+1] += 1
            if jj > 0:
              octs[ii+1,jj-1] += 1
  
  for me in flashed:
    octs[me[0],me[1]] = 0
  # print(octs.transpose())
print(f"They simul flash on step {step}.")