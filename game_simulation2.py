import random

def hit_quality(batter_average):
    bases_hit = 0
    for i in range(4):
        if batter_average > random.random():
            bases_hit += 1
        else:
            break
    return bases_hit


def single_inning_score(on_base, batting_average, lineup_indices): 
    runs = 0
    current_bases = [0] * 4
    outs = 0
    while outs < 3:
        for batter in lineup_indices:
            batter_average = (on_base[batter] + batting_average[batter]) / 2
            bases_hit = hit_quality(batter_average)
            if bases_hit == 0:
                outs += 1
                if outs >= 3:
                    break
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
    return runs
    
    
def final_score(nlineup, on_base, batting_average, lineup_indices):
    total_runs = 0
    for i in range(nlineup):
        total_runs += single_inning_score(on_base, batting_average, lineup_indices)
    return total_runs