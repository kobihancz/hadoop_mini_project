#!/usr/bin/env python
import sys
# from csv import reader
# import csv

# with open('/Users/kobihancz/Downloads/Springboard Data engineering/hadoop_mini_project/mapper2_out.csv','w') as outfile:
#     with open('/Users/kobihancz/Downloads/Springboard Data engineering/hadoop_mini_project/reducer1_out.csv','r') as infile:
#         csv_reader = reader(infile)
#         for line in csv_reader:
# for line in sys.stdin:
#     strl = " "
#     string = strl.join(line)
#     key, value = string.split("\t")
#     value = value.split(" ")

#     key = value[1]+value[2]
#     value = 1
    
#     print('%s\t%s' % (key,value))
    # outfile.write('%s\t%s' % (key,value))
    # outfile.write('\n')
for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")
    print(f'{key}\t{value}')
        