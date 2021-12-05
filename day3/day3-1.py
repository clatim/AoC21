import numpy as np


with open('input3.txt', 'rb') as f:
  max_bits = 0
  for line in f:
    # Find the longest number so we know how many bitwise ands we need
    # to do
    if len(line.strip()) > max_bits:
      max_bits = len(line.strip())
  print (f"The longest entry is {max_bits} long.")
  # Set up an array to hold the average value of a bit
  avg_bit = np.zeros(max_bits)
  # Reset the file to the start
  f.seek(0)
  num_entries = 0
  for line in f:
    # Ok strip end of line off and convert to integer so we can do
    # bitwise operations
    val = int(line.strip(), 2)
    num_entries += 1
    for ii in range(max_bits):
      avg_bit[ii] += (val & 2**ii)/2**ii
    

  # Note the bits are reversed here
  avg_bit = avg_bit/num_entries
  # initialise rates to 0
  gamma_rate = 0
  epsilon_rate = 0
  for ii in range(max_bits):
    if avg_bit[ii] >= 0.5:
      gamma_rate += 2**ii
    else:
      epsilon_rate += 2**ii
  print(f"Product of gamma and epsilon rates is {gamma_rate*epsilon_rate}")

  f.seek(0)
  # find the oxygen and c02 rate
  oxy_nums =[]
  c02_nums = []
  for line in f:
    val = int(line.strip(), 2)
    oxy_nums.append(val)
    c02_nums.append(val)

  for ii in range(max_bits-1,-1,-1):
    #find most common bit
    if len(oxy_nums) != 1:
      avg = 0
      for val in oxy_nums:
        avg += (val & 2**ii)/2**ii
      avg = 1 if avg/len(oxy_nums) >= 0.5 else 0
      oxy_nums = [val for val in oxy_nums if val & 2**ii == 2**ii*avg]
    
    if len(c02_nums) != 1:
      avg = 0
      for val in c02_nums:
        avg += (val & 2**ii)/2**ii
      avg = 0 if avg/len(c02_nums) >= 0.5 else 1
      c02_nums = [val for val in c02_nums if val & 2**ii == 2**ii*avg]

  print(f"Product oxygen and c02 is {oxy_nums[0]*c02_nums[0]}")

      
