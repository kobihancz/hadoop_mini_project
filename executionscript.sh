#!/bin/bash

hadoop jar /usr/local/opt/hadoop/libexec/share/hadoop/common/hadoop-streaming-3.3.1.jar \
-file /Users/kobihancz/Downloads/Springboard_Data_Engineering/hadoop_mini_project/mapper1.py -mapper "python3 mapper1.py" \
-file /Users/kobihancz/Downloads/Springboard_Data_Engineering/hadoop_mini_project/reducer1.py -reducer "python3 reducer1.py" \
-input /test_directory/hadoop_mini_project/data.csv -output /test_directory/hadoop_mini_project/output/all_accidents \
2> execution_report.log

hadoop jar /usr/local/opt/hadoop/libexec/share/hadoop/common/hadoop-streaming-3.3.1.jar \
-file /Users/kobihancz/Downloads/Springboard_Data_Engineering/hadoop_mini_project/mapper2.py -mapper "python3 mapper2.py" \
-file /Users/kobihancz/Downloads/Springboard_Data_Engineering/hadoop_mini_project/reducer2.py -reducer "python3 reducer2.py" \
-input /test_directory/hadoop_mini_project/output/all_accidents -output /test_directory/hadoop_mini_project/output/make_year_count \
2> execution_report.log