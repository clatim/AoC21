import numpy as np

# Set up a dict with the keys as the closing braces and the values as the opening
# braces
d = {
  ')':'(',
  ']':'[',
  '}':'{',
  '>':'<'
}

scores = {
  ')':3,
  ']':57,
  '}':1197,
  '>':25137
}

total_score = 0
valid_lines = []
with open('input10.txt','r') as f:
  for line in f:
    close_me = []
    corrupt = False
    for char in line.strip():
      if char in d.values():
        close_me.append(char)
      elif char in d.keys():
        if close_me[-1] == d[char]:
          # If it matches the last open one then remove the open one
          # and carry on scanning the line
          close_me.pop(-1)
        else:
          print(f"Corrupt line with corrupt character {char}")
          total_score += scores[char]
          corrupt = True
          break
      else:
        print(f"Invalid character")
    
    if not corrupt:
      valid_lines.append(line.strip())

print(f"The final score for part 1 is {total_score}")

print("Now score the incomplete lines")
scores_part2 = {
  '(':1,
  '[':2,
  '{':3,
  '<':4
}

auto_scores = np.zeros(len(valid_lines),dtype='int')
for ii, line in enumerate(valid_lines):
  close_me=[]
  for char in line:
    if char in d.values():
      close_me.append(char)
    elif char in d.keys():
      if close_me[-1] == d[char]:
        close_me.pop(-1)
    
  # Loop over backwards to ensure we score properly
  for char in reversed(close_me):
    auto_scores[ii] = 5*auto_scores[ii] + scores_part2[char]
      
auto_scores = np.sort(auto_scores)
winning_index = np.ceil(auto_scores.size/2).astype('int') - 1 # -1 for zero index.....
print(f"And the auto complete wining score is {auto_scores[winning_index]}")