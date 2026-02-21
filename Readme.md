# Run Hadoop in docker

### Install docker & docker compose
macos: https://docs.docker.com/desktop/setup/install/mac-install/

windows: https://docs.docker.com/desktop/setup/install/windows-install/

### Run Hadoop on docker compose

start container
```
docker compose up -d
```

# MapReduce

modify file `./mapper.py` and `./reducer.py`

modify file `./input.txt` for test data

# Create output file via HDFS

run `execute.sh`
```
./execute.sh
```
> Note: if no permission to execute try `chmod +x ./execute.sh`

output file will be store in `/user/root/output`

checking result of output file using this command
```
docker exec -it namenode hdfs dfs -cat /user/root/output/part-00000
```
<!--
# View data in Hive

connect to hive using `localhost:10000`

create table in Hive (modify columns based on output file)
```
CREATE EXTERNAL TABLE assignment_01(
	  person_id INT,
    district_id INT,
    avg_income DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
LOCATION '/user/root/output';
``` -->
