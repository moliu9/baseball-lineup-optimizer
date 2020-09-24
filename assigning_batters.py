import numpy as np
import csv

#this function parses and normalize the stats of each player
def read_stats():
    csv_file = open("batting_line_up_data.csv")
    total_row = sum(1 for row in csv_file) - 1
    csv_file.seek(0)
    csv_reader = csv.reader(csv_file, delimiter = ",")
    batting_average = np.zeros((total_row,))
    on_base = np.zeros((total_row,))
    slugging = np.zeros((total_row,))
    strike_out = np.zeros((total_row,))
    stolen_bases = np.zeros((total_row,))
    batter_names = [None] * total_row 
    i = 0 
    for row in csv_reader:
        if i != 0:
            batter_names [i-1] = row[0]
            batting_average [i-1] = (float(row[1]) - .177)/.169
            on_base [i-1] = (float(row[2]) - .232)/.206
            slugging [i-1] = (float(row[3]) - .279)/.361
            strike_out [i-1] = 1 - (float(row[4]) - .144)/.145
            stolen_bases [i-1] = (float(row[5]) - 1)/29
        i += 1
    csv_file.close()
    return batting_average, on_base, slugging, strike_out, stolen_bases, batter_names

#this function finds the index of each batter and create an array so the names could be related to the indices
def find_batter_index(batter, batter_names):
    return batter_names.index(batter)

#this function selects the batters based on their individual abilities
def get_lineup():
    
    def assign_3rd_batter(batting_average):
        for i in batting_average:
            index = np.argmax(batting_average)
            third_batter = batter_names[index]
            batting_average[index] = 0
            stolen_bases[index] = 0
            on_base[index] = 0
            slugging[index] = 0
            strike_out[index] = 0
            return third_batter
            
    def assign_1st_batter(stolen_bases, on_base):
        first_batter_combo = 0.2*stolen_bases + 0.8*on_base
        for i in first_batter_combo:
            index2 = np.argmax(first_batter_combo)
            first_batter = batter_names[index2]
            batting_average[index2] = 0
            stolen_bases[index2] = 0
            on_base[index2] = 0
            slugging[index2] = 0
            strike_out[index2] = 0
            return first_batter
    
    def assign_4th_5th_6th_batter(batting_average, slugging, strike_out):
        fourth_batter_combo = 0.55*batting_average + 0.3*slugging + 0.15*strike_out
        for i in fourth_batter_combo:
            index3 = np.argmax(fourth_batter_combo)
            fourth_batter = batter_names[index3]
            batting_average[index3] = 0
            stolen_bases[index3] = 0
            on_base[index3] = 0
            slugging[index3] = 0
            strike_out[index3] = 0
            return fourth_batter
        
    def assign_2nd_9th_batter(stolen_bases, on_base):
        second_batter_combo = 0.3*stolen_bases + 0.7*on_base
        for i in second_batter_combo:
            index4 = np.argmax(second_batter_combo)
            second_batter = batter_names[index4]
            batting_average[index4] = 0
            stolen_bases[index4] = 0
            on_base[index4] = 0
            slugging[index4] = 0
            strike_out[index4] = 0
            return second_batter
        
    def assign_7th_8th_batter(on_base):
        index5 = np.argmax(on_base)
        seventh_batter = batter_names[index5]
        batting_average[index5] = 0
        stolen_bases[index5] = 0
        on_base[index5] = 0
        slugging[index5] = 0
        strike_out[index5] = 0
        return seventh_batter
    
    batting_average, on_base, slugging, strike_out, stolen_bases, batter_names = read_stats()
    batting_average_c, on_base_c, slugging_c, strike_out_c, stolen_bases_c, batter_names_c = read_stats()
    
    third_batter = assign_3rd_batter(batting_average)
    first_batter = assign_1st_batter(stolen_bases, on_base)
    fourth_batter = assign_4th_5th_6th_batter(batting_average, slugging, strike_out)
    second_batter = assign_2nd_9th_batter(stolen_bases, on_base)
    fifth_batter = assign_4th_5th_6th_batter(batting_average, slugging, strike_out)
    sixth_batter = assign_4th_5th_6th_batter(batting_average, slugging, strike_out)
    ninth_batter = assign_2nd_9th_batter(stolen_bases, on_base)
    seventh_batter = assign_7th_8th_batter(on_base)
    eighth_batter = assign_7th_8th_batter(on_base)
    
    lineup = [first_batter, second_batter, third_batter, fourth_batter, fifth_batter, sixth_batter, seventh_batter, eighth_batter, ninth_batter]
    
    def find_batter_index_local(batter):
        return find_batter_index(batter, batter_names)
    
    return list(map(find_batter_index_local, lineup)), batter_names
    