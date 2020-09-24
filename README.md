# Baseball Statistics

Our program takes in batting statistics (batting average, on base percentage, slugging percentage, stolen bases, and strike out percentage) from a team and uses optimization functions (unique to each batter) to return the best lineup, which will maximize the amount of runs scored. It then tests this hypothesized lineup by simulating a game by running through the batting lineup over nine innings by looking at who is on base and the chance of the batter to get on base to determine the final score of the game. The computer generated lineup using our program was run as well as a random lineup to compare the results and determine if the program which generated a lineup using stats was effective.

After the maximized lineup is generated, a theoretical score of the team could be generated using the game simulation. Bear in mind that the score considers only the ability of the players and not the opponents, and therefore the total runs scored is likely higher than that of an actual game. Runs scored in a single inning is calculated based whether the hitter was able to hit a single, double, triple, or a homerun, and the function iterates through every single batter on the lineup until the number of outs in an inning reaches three. In the end, the score from each inning is added to the final score. The simulation is repeated as much as the user desires and its results are visually represented in a histogram. 

## Instructions

Open main.py. The lineup can be changed by editing the variable "lineup". The arbitrary lineup (which bats the hitters in order of which they were listed in the data file) can be tested by making lineup = arbitrary_lineup (which is defined earlier). The number of innings can also be changed to see the progression of the game, for example, how many runs a this maximized lineup will have by the fourth inning versus a random lineup. The title of the histogram can also be changed to reflect the lineup being tested.

In order to test another teams' statistics, a user will need to go into the assigning_batters.py script and change the name of the file being imported. Additionally, the data was normalized using the Red Sox data. This is done by taking each data point and subtracting the lowest data point in a given category and dividing by the biggest data point - smallest data point.

## File List

batting_llineup_data.csv: the file containing categorical statistics of each of the nine batters.

assigning_batters.py: parses the statistics from the csv file and organizes them into separate arrays. A maximized, indexed, lineup is generated using various functions to weight the most important categories for each batting position.

game_simulation.py: uses a few of the statistc arrays and the maximized lineup generated to simulate a baseball game and records the scores.

main.py: user inputs the lineup data and other paramters to generate a distribution of total runs scored by that particular lineup.
