import numpy as np
from kaggle_environments import make, evaluate

# Selects random valid column
def agent_random(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return random.choice(valid_moves)

# Selects middle column
def agent_middle(obs, config):
    return config.columns//2

# Selects leftmost valid column
def agent_leftmost(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return valid_moves[0]

# install requests
import random



# let's make a smarter game agent
# how about an agent that makes a winning move if it can, and a random valid move otherwise

# start by coding the agent, we'll need to create some helper functions along the way
# add the obs and config as input to the functions

# obs contains two pieces of information:
#       obs.board - the game board (a Python list with one item for each grid location)
#       obs.mark - the piece assigned to the agent (either 1 or 2)
# config contains three pieces of information:
#       config.columns - number of columns in the game board (7 for Connect Four)
#       config.rows - number of rows in the game board (6 for Connect Four)
#       config.inarow - number of pieces a player needs to get in a row in order to win (4 for Connect Four)
# col is any valid move
# piece is either the agent's mark or the mark of its opponent


# create a list of valid moves (0 to the number of columns)

# for each move, check if it's the winning move

# if it is, return that move
# else, return a random play

def agent_q1(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]

    for move in valid_moves:
        # lets make a check winning move function function, returns true if winning move
        if check_winning_move(obs, config, move, obs.mark):
            return move

    return random.choice(valid_moves)



# Returns True if dropping piece in column results in game win

# first we need to convert the board to a grid - lets use numpys reshape function
# create a new grid with the piece dropped in the col specified
# lets create a function for this called drop_piece

def check_winning_move(obs, config, col, piece):
    # Convert the board to a 2D grid
    grid = np.asarray(obs.board).reshape(config.rows, config.columns)

    next_grid = drop_piece(grid, col, piece, config)
    # horizontal
    for row in range(config.rows):
        for col in range(config.columns-(config.inarow-1)):
            window = list(next_grid[row,col:col+config.inarow])
            if window.count(piece) == config.inarow:
                return True
    # vertical
    for row in range(config.rows-(config.inarow-1)):
        for col in range(config.columns):
            window = list(next_grid[row:row+config.inarow,col])
            if window.count(piece) == config.inarow:
                return True
    # positive diagonal
    for row in range(config.rows-(config.inarow-1)):
        for col in range(config.columns-(config.inarow-1)):
            window = list(next_grid[range(row, row+config.inarow), range(col, col+config.inarow)])

            if window.count(piece) == config.inarow:
                return True
    # negative diagonal
    for row in range(config.inarow-1, config.rows):
        for col in range(config.columns-(config.inarow-1)):
            window = list(next_grid[range(row, row-config.inarow, -1), range(col, col+config.inarow)])
            if window.count(piece) == config.inarow:
                return True
    return False




# Gets board at next step if agent drops piece in selected column

# start by copying the grid object by usingthe .copy() function
def drop_piece(grid, col, piece, config = { 'rows': 3 }):
    next_grid = grid.copy()
    for row in range(config.rows-1, -1, -1):
        if next_grid[row][col] == 0:
            break
    next_grid[row][col] = piece
    return next_grid




import random

# an agent that selects a winning move if one exists, otherwise random


# selects a winning move if one exists, checks if it can block a winning move by opponent,
# else plays random
def agent_q2(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]

    for move in valid_moves:
        if check_winning_move(obs, config, move, obs.mark):
            return move

    opponents_mark = int(not (obs.mark - 1)) + 1

    for move in valid_moves:
        if check_winning_move(obs, config, move, opponents_mark):
            return move

    return random.choice(valid_moves)


# Create the game environment
# Set debug=True to see the errors if your agent refuses to run
env = make("connectx", debug=True)

# Two random agents play one game round
env.run([agent_q1, agent_random])

# Show the game
with open("data.html", "w") as file:
    file.write(str(env.render(mode="html")))


def get_win_percentages(agent1, agent2, n_rounds=100):
    # Use default Connect Four setup
    config = {'rows': 6, 'columns': 7, 'inarow': 4}
    # Agent 1 goes first (roughly) half the time
    outcomes = evaluate("connectx", [agent1, agent2], config, [], n_rounds//2)
    # Agent 2 goes first (roughly) half the time
    outcomes += [[b,a] for [a,b] in evaluate("connectx", [agent2, agent1], config, [], n_rounds-n_rounds//2)]
    print("Agent 1 Win Percentage:", np.round(outcomes.count([1,-1])/len(outcomes), 2))
    print("Agent 2 Win Percentage:", np.round(outcomes.count([-1,1])/len(outcomes), 2))
    print("Number of Invalid Plays by Agent 1:", outcomes.count([None, 0]))
    print("Number of Invalid Plays by Agent 2:", outcomes.count([0, None]))


get_win_percentages(agent_q1, agent_random, 500)