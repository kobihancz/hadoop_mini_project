#!/usr/bin/env python
import sys
# from csv import reader;

# master_info = {}

# def flush(vin):
#     key = vin
#     value = master_info[vin]
#     value[0] = 'A'
#     value = value[0]+' '+value[1]+' '+value[2]
#     print('%s\t%s' % (key,value))
#     # outfile.write('%s\t%s' % (key,value))
#     # outfile.write('\n')

# #test code that will be replaced by the for loop that reads from standard in        
# # with open('/Users/kobihancz/Downloads/Springboard Data engineering/hadoop_mini_project/reducer1_out.csv','w') as outfile:    
# #     with open('/Users/kobihancz/Downloads/Springboard Data engineering/hadoop_mini_project/mapper1_out.csv','r') as infile:
# #         csv_reader = reader(infile)
# #         for line in csv_reader:
# for line in sys.stdin:    
#     strl = " "
#     string = strl.join(line)
#     key, value = string.split("\t")
#     value = value.split(" ")

#     vin = key
#     incident_type = value[0]
    

# # parse input from mapper and update master info
#     if incident_type == 'I':
#         master_info[vin] = value
#     elif incident_type == 'A':
#         flush(vin)

master_info = {}

#writes propogated data to standard out 
def flush():
    for key in master_info.keys():
        # Prints make, year and accident_count
        print(f'{(master_info[key]["make"], master_info[key]["year"])}\t{master_info[key]["accident_count"]}')

for line in sys.stdin:
    line = line.strip()
    vin_number, values = line.split('\t')
    
    # List comprehension to remove unnecessary characters and extract desired values.
    values_list = [val.replace("'", "").replace("(", "").replace(")", "").replace(" ", "") for val in values.split(",")]
    incident_type = values_list[0]
    vehicle_make = values_list[1]
    vehicle_year = values_list[2]

    # check if vin is in dict
    if vin_number not in master_info:
        master_info[vin_number] = {"make": None, "year": None, "accident_count": 0}

    # grab vehicle make and year from master_info, only where incident type == I
    if incident_type == "I":
        master_info[vin_number]["make"] = vehicle_make
        master_info[vin_number]["year"] = vehicle_year

    #increment count for each incident type == A
    if incident_type == "A":
        master_info[vin_number]["accident_count"] += 1

flush()




























