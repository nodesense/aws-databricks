Windows search, Anaconda prompt

pip install boto3

pip install findspark

python progrma.py

----

input [1..9]

parallelize(input)

spark move the data into partition

hashcode/key 

partition is subset
within partition, the data is ordered in same way it arrived
p0 : [1,4, 5]
p1 : [6, 7]
p2 : [2, 3, 8, 9]


Tasks
    map
    filter

TaskRunner
    map tasks from scheduler
    task is assigned to p0
    1 => 10 map (n => n * 10)
    4 => 40
    5 => 50

    --
    map tasks from scheduler
    task is assigned to p1
    6 => 60
    7 => 70
    --
    task with p2
    2 => 20 
    3 => ..
    8..
    9 => 90


     rdd = sc.parallelize(input, 1) 1 present the partition numbers

     p0: [1,2,3,4,5,6,7,8,9]




0 to 1

4 partitons 

(key, value)

(IN, {amount: 1000, ...}) HASHCODE % MAX_PARITION 48 % 4 - 0 P0
(IN, {amount: 2000, ...}) 48 % 4 - P0
(UK, {amount: 6000, ...}) 54 % 4 - P2
(USA, {amount: 6000, ...}) 53 % 4 - P1
(IN, {amount: 1\4000, ...})
(IN, {amount: 6000, ...})

hashcode(IN) - 48
hashcode(IN) - 48
hashcode(USA) - 53
hashcode(UK) - 54
...

MAX Partitions: = 4
p0- [(IN, {amount: 1000, ...}), (IN, {amount: 2000, ...}), (IN, {amount: 1\4000, ...}), (IN, {amount: 6000, ...})]
p1 - (USA, {amount: 6000, ...})
p2 - [(UK, {amount: 6000, ...})]
p3 - []
p4 - []

--

MAX : 2


(IN, {amount: 1000, ...})  48 % 2 - 0 P0
(IN, {amount: 2000, ...}) 48 % 2 - P0
(UK, {amount: 6000, ...}) 54 % 2 - P0
(USA, {amount: 6000, ...}) 53 % 2 - P1
(IN, {amount: 1\4000, ...}) - P0
(IN, {amount: 6000, ...}) - p0

p0 - (IN, {amount: 1000, ...}), (IN, {amount: 2000, ...}), (IN, {amount: 1\4000, ...}), (IN, {amount: 6000, ...}),  (USA, {amount: 6000, ...})
p1 -  [(UK, {amount: 6000, ...})]

groupByKey - 
    count()/sum()

HDFS
    100 MB
        16 MB - P0
        16 MB - P1






Row ( name, role....)

POJO
class EMployee {
    String name;
    String role;
    //get/set   
}

Serialiation
    xml
    json
    java
    avro.
    ..
    Spark binary object encoder - Use this


[
{
    name: 'Krish',
    role: 'Mentor'
},
{

}
]



DF -> column/type -> JVM -> create bytecodes that represent object in JVM -- POJO Employee, employee rdd

====================================

CAtalog
    Meta Data
        table  orders table
                    id string, amount flow, date long, ipaddre string........

        where the files are stored, 
            s3 bucket
            location: s://e-commecer/orders


Query Engine NOT THE DB, NO PERSISTENT STORAGE: Athena, it will understand meta data from data lake formation
            select id, amount from orders; --> written back to s3

Data Lake
    s3
        bucket/folder/file -- key
        ..
        ..
        e-commecer/orders
                        order1.csv
                        order2.csv
                        ...
                         columns (id, amount, date, ip_address...)




-----

conda create --name dbconnect python=3.7

pip install -U databricks-connect==6.4.*
 
---

clusterid

0119-150258-goat1


The port that Databricks Connect connects to. Set to 15001.

databricks-connect configure



databricks-connect test


open file
%APPDATA%\Code\User\settings.json


paste below

   "python.venvPath": "c:/Users/Gopalakrishnan/miniconda3",
    "python.linting.enabled": false


    sudo apt install postgresql-client-12

psql -U postgres -h productdb.cd2jj5yzqenx.eu-central-1.rds.amazonaws.com -p 5432 postgres

pass  Avv$9753!


create database testdb;
\c testdb;
