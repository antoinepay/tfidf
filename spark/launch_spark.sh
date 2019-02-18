#!/usr/bin/env bash

hdfs dfs -put corpus/0 /user/hadoop/corpus
spark-submit --master yarn \
--executor-memory 7g \
—-num-executors 5 \
-—executor-cores 1 \
spark_instructions.py

hdfs dfs -put corpus/1 /user/hadoop/corpus
spark-submit --master yarn \
--executor-memory 7g \
—-num-executors 5 \
-—executor-cores 1 \
spark_instructions.py

hdfs dfs -put corpus/2 /user/hadoop/corpus
spark-submit --master yarn \
--executor-memory 7g \
—-num-executors 5 \
-—executor-cores 1 \
spark_instructions.py

hdfs dfs -put corpus/3 /user/hadoop/corpus
spark-submit --master yarn \
--executor-memory 7g \
—-num-executors 5 \
-—executor-cores 1 \
spark_instructions.py

hdfs dfs -put corpus/4 /user/hadoop/corpus
spark-submit --master yarn \
--executor-memory 7g \
—-num-executors 5 \
-—executor-cores 1 \
spark_instructions.py

