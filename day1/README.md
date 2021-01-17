Google chrome 

https://adoptopenjdk.net/?variant=openjdk8&jvmVariant=hotspot

https://repo.anaconda.com/miniconda/Miniconda3-py37_4.9.2-Windows-x86_64.exe

https://code.visualstudio.com/download

Python and AWS Cli plugins

https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC


Open CMD

 > javac -version
 > java -version
 > echo %JAVA_HOME%
 > 



 create a directory called .aws in C:\Users\Administrator

   create files called credentials 
   create file called config


Download https://www.7-zip.org/a/7z1900-x64.msi


https://www.nic.funet.fi/pub/mirrors/apache.org/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz


extract and keep in c: drive

set SPARK_HOME to C:\spark-2.4.7-bin-hadoop2.7
add C:\spark-2.4.7-bin-hadoop2.7\bin to PATH


https://archive.apache.org/dist/hadoop/common/hadoop-2.7.7/hadoop-2.7.7.tar.gz

extract and keep in c:

set HADOOP_HOME to C:\hadoop-2.7.7

donwload winutils.exe and move to HADOOP_HOME/bin

https://github.com/steveloughran/winutils/tree/master/hadoop-2.7.1/bin

https://gitforwindows.org/


Open Command Prompt 

cd %SPARK_HOME%\bin

> pyspark





Install AWS Cli

https://awscli.amazonaws.com/AWSCLIV2.msi

Node.js 

https://nodejs.org/en/download/


---

Search Anaconda in windows  and use that command prompt

We use Python 3.7, Spark doesn't support 3.8 on Spark 2.4
We use Spark 2.4


For Scala. Not part of this training

IntelliJ community Edition

https://www.jetbrains.com/idea/download/download-thanks.html?platform=windows&code=IIC

Add Scala Plugin

----

Jupyter notebook

Open Anacond data command propt

conda install -c conda-forge jupyterlab

Yes to install all plugs in

---

To start jupyter,

> jupyter-lab


http://localhost:8888/lab

Create notebooks directory in Documents



---

Try pyspark cli

---
Pyspark with jupyter

open anaconda cmd line

then 

cmd

set PYSPARK_DRIVER_PYTHON=jupyter
set PYSPARK_DRIVER_PYTHON_OPTS='notebook'

pyspark
---

or set windows env variables

setx PYSPARK_DRIVER_PYTHON jupyter
setx PYSPARK_DRIVER_PYTHON_OPTS 'notebook'


set PYSPARK_DRIVER_PYTHON=

set PYSPARK_DRIVER_PYTHON_OPTS=


REG delete HKCU\Environment /F /V PYSPARK_DRIVER_PYTHON
REG delete HKCU\Environment /F /V PYSPARK_DRIVER_PYTHON_OPTS



pyspark
----


