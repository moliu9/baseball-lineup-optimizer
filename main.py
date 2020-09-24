"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions
# IMPORT STATEMENTS
from assigning_batters import *
from game_simulation import *
import numpy as np
import matplotlib.pyplot as plt

# DEMONSTRATION CODE

batting_average, on_base, slugging, strike_out, stolen_bases, batter_names = read_stats()

#prints out the maximized lineup:
lineup_indices, batter_names = get_lineup()
print('Batting Lineup:')
for i, batter_index in enumerate(lineup_indices):
    print(str(i+1) + ". " + batter_names[batter_index])
 
#creating an arbiturary lineup:
arbitrary_lineup = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#testing the score of the game:
score = np.zeros(50000) #this number could be changed based on how many trials the user would like to run
for i in range(50000):
    innings = 9
    lineup = lineup_indices
    score[i] = final_score(innings, on_base, batting_average, arbitrary_lineup)
average_score = score.mean()
print("\n Average Total Run: " + str(average_score))

#creates a histogram of the score distribution 
plt.hist(score, bins = np.linspace(0, 50, 51) + 0.5)
plt.title("Final Score Distribution")
plt.xlabel("Runs Scored")
plt.ylabel("# of Games")