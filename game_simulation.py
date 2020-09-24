import random

#this function determines how many bases a single batter can hit based on their stats
def hit_quality(batter_average): 
    bases_hit = 0
    for i in range(4):
        if 0.9 * batter_average > random.random():
            bases_hit += 1
        else:
            break
    return bases_hit

#this function returns score of a single inning and keeps tracks of the place in the lineup so that the batter next in line can start in the following inning. 
def single_inning_score(on_base, batting_average, lineup_indices, current_batter_index): 
    runs = 0
    current_bases = [0] * 4
    outs = 0
    while outs < 3:
        batter = lineup_indices[current_batter_index]
        batter_average = (on_base[batter] + batting_average[batter]) / 2
        bases_hit = hit_quality(batter_average)
        if bases_hit == 0:
            outs += 1
        if bases_hit == 1:
            current_bases = [1] + current_bases[0:3]
            runs += int(current_bases[3])
        if bases_hit == 2:
            current_bases = [1] + current_bases[0:3]
            runs += int(current_bases[3])
            current_bases = [0] + current_bases[0:3]
            runs += int(current_bases[3])
        if bases_hit == 3:
            current_bases = [1] + current_bases[0:3]
            runs += int(current_bases[3])
            current_bases = [0] + current_bases[0:3]
            runs += int(current_bases[3])
            current_bases = [0] + current_bases[0:3]
            runs += int(current_bases[3])
        if bases_hit == 4:
            current_bases[3] = 0
            runs += sum(current_bases) + 1
            current_bases = [0] * 4
        current_batter_index = (current_batter_index + 1) % len(lineup_indices)
    return runs, current_batter_index
    
#this function iterates the inning 9 times and returns the final score of the game. 
def final_score(nlineup, on_base, batting_average, lineup_indices):
    curr_index = 0
    total_runs = 0
    for i in range(nlineup):
        p_index = curr_index
        runs, curr_index = single_inning_score(on_base, batting_average, lineup_indices, curr_index)
        total_runs += runs
    return total_runs