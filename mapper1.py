#!/usr/bin/env python
import sys
# from csv import reader
# import csv



#test code to view output
# with open('/Users/kobihancz/Downloads/Springboard Data engineering/hadoop_mini_project/mapper1_out.csv','w') as outfile:
#     with open('/Users/kobihancz/Downloads/Springboard Data engineering/hadoop_mini_project/data.csv','r') as infile:
#         csv_reader = reader(infile)
#         for line in csv_reader: 

# for line in sys.stdin:
#     key = line[2]
#     print(line)
#     value = line[1]+' '+line[3]+' '+line[5]
    # print('%s\t%s' % (key,value))
    # outfile.write('%s\t%s' % (key,value))
    # outfile.write('\n')
for line in sys.stdin:
    line = line.strip()
    data = line.split(',')
    # Print/Map out values as combination of vin_number and tuple
    print(f"{data[2]}\t{(data[1], data[3], data[5])}")    