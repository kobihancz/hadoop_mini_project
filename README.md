# hadoop_mini_project

### Description:
In this mini-project the goal was to write a MapReduce program that produced a report of the total number of accidents per make and year of the car. Since there was missing data in the accident records, I did this by populating the missing values from incident reports into the accident report records. This was miltiple step process that started with sripting 4 python files(2 mappers and 2 reducers). Each file used the output of the previouse file starting with the given data. I then downloaded Hadoop's distributed file system locally onto my OS and used a bash script to run the mapreduce job.  

### Files
1. ```mapper1.py``` - Maps the vin_number, make, year and incident type from every record in ```data.csv```.
2. ```reducer1.py``` - Creates master Python dictionary used to keep track of records with incident_type "I" to populate make and year. We filter through incident_type "A" in order to update and automatically increment the "accident_count" by 1 based on occurrence.
3. ```mapper2.py``` - Map out the make and year as key, and accident_count as a value.
4. ```reducer2.py``` - Aggregate (reduce) and collect final count for every make and year combination.
5. ```execution_report.log``` - All of the messages from using terminal to execute bash script and run the mapreduce job in hadoop.
6. ```solution.log``` - the solution resulting from running the mapreduce job .
7. ```data.csv``` - the initial car report data provided

### How to test Python script using Python 3
```
cat data.csv | python3 mapper1.py | reducer1.py | mapper2.py | reducer2.py
```

### How to run bash script
1. First you will need to download Hadoop version 3.3.1 locally, along with java 1.8
2. you will then start haddop by running the command ``` ./start-all.sh   ```
3. Then you will need to make sure its running corectly using the command ``` jps ``` it should look like this
```
35538 NameNode
35781 SecondaryNameNode
35975 ResourceManager
50504 Jps
35642 DataNode
36075 NodeManager
```
3. once its running correctly you can run the bash script with the command ``` bash executionscript.sh   ```
4. stop running hadoop by using the command ``` ./stop-all.sh   ```

