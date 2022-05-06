from kaggle_environments import make, evaluate
# install requests
import random

# Create the game environment
# Set debug=True to see the errors if your agent refuses to run
env = make("connectx", debug=True)

# List of available default agents
print(list(env.agents))

# Two random agents play one game round
env.run(["random", "random"])

# Show the game
with open("data.html", "w") as file:
    file.write(str(env.render(mode="html")))



