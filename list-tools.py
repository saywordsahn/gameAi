import numpy as np

# how the board looks
board = [0, 0, 0, 0, 1, 0, 1, 0, 2]
# convert to 2d array to make it easier to understand
grid = np.asarray(board).reshape(3, 3)

print(board)
print(grid)


# get a window of the 1d array
window1d = board[3: 6]
print(window1d)


# get a window of a 2d array
window2d = grid[1:3, 1:3]
print(window2d)