import numpy as np

with open("input4.txt", 'r') as f:
  lines = f.readlines()
  # Read in the numbers to be drawn
  draws = np.array([int(x) for x in lines[0].strip().split(",")])
  print(draws)
  
  left2read = True
  lines = [line.strip().split() for line in lines]
  boards = []
  ct = 0
  # Read in the boards
  while left2read:
    # Try and read the next board
    start = 2+5*ct+ct
    end = 2+5*(ct+1)+ct
    board = np.asarray(lines[start:end]).astype('int')
    if board != []:
      boards.append(board)
      ct = ct+1
      # Get the suffix correct cause why not.
      if str(ct)[-1] == '1':
        suffix = 'st'
      elif str(ct)[-1] == '2':
        suffix = 'nd'
      elif str(ct)[-1] == '3':
        suffix = 'rd'
      else:
        suffix = 'th'
      print(f"I have added a {ct}{suffix} board.")
    else:
      left2read = False
  
  print(f"I have read all of the boards. There were {ct} of them.")

  # If false, we look and score the first winning board
  # if true, we look and score the last winning board
  squid_win = True
  winning_boards = np.zeros(len(boards))

  # Now start reading off of the numbers
  for draw in draws:
    # Check if an entry is in a board, if it is, see if it is the last one
    # in that row of column. If it is the last one, we have a winner
    # If it isn't, then just zero it and carry on.
    print(f"Value drawn is {draw}")
    for ii, board in enumerate(boards):
      if np.any(board == draw):
        row, col = np.where(board == draw)
        row, col = row[0], col[0]
        # Set them to -1. I tried 0 but turns out 0 can be an entry on a board
        board[row,col] = -1
        if np.all(board[row,:] == -1) or np.all(board[:,col] == -1):
          winning_boards[ii] = 1
          if np.all(winning_boards==1) and squid_win:
            winning_val = draw
            winning_board = board[board>=0]
            print (f"The last board has won on value {winning_val}...")
            break
          else:
            winning_val = draw
            winning_board = board[board>=0]
            print(f"We have a winner on value {winning_val}!")
            break
        
    else:
      continue
    break

  
  print(f"And the winning score is {np.sum(winning_board)*winning_val}")
