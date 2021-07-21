#!/usr/bin/env python
import sys
# from csv import reader

# master_info = {}

# def flush():
#     for key in master_info:
#         print(key, master_info[key])

   
# # with open('/Users/kobihancz/Downloads/Springboard Data engineering/hadoop_mini_project/mapper2_out.csv','r') as infile:
# #     csv_reader = reader(infile)
# #     for line in csv_reader:
# for line in sys.stdin:   
#     strl = " "
#     string = strl.join(line)
#     key, value = string.split("\t")
#     value = int(value)
    
#     if key not in master_info:
#         master_info[key] = value
#     elif key in master_info:
#         master_info[key] += 1
# flush()


acc_count_info = {}

#flush out make and year as key and count as value
def flush():
    for key in acc_count_info.keys():
        print(f'{key}\t{acc_count_info[key]}')

for line in sys.stdin:
    line = line.strip()
    make_year, acc_count = line.split('\t')

    # remove unwanted charachters
    acc_count = int(acc_count.replace("'", "").replace("(", "").replace(")", ""))

    # if input key is not already in dict, make a new entry
    if make_year not in acc_count_info:
        acc_count_info[make_year] = 0
    acc_count_info[make_year] += acc_count

flush()
