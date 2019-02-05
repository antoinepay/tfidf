#!/usr/bin/env bash

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/hadoop/wc/input \
-output /user/hadoop/wc/output1 \
-file /home/hadoop/mapper_1.py \
-mapper /home/hadoop/mapper_1.py \
-file /home/hadoop/reducer_1.py \
-reducer /home/hadoop/reducer_1.py

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/hadoop/wc/output1 \
-output /user/hadoop/wc/output2 \
-file /home/hadoop/mapper_2.py \
-mapper /home/hadoop/mapper_2.py \
-file /home/hadoop/reducer_2.py \
-reducer /home/hadoop/reducer_2.py

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/hadoop/wc/output2 \
-output /user/hadoop/wc/output3 \
-file /home/hadoop/mapper_3.py \
-mapper /home/hadoop/mapper_3.py \
-file /home/hadoop/reducer_3.py \
-reducer /home/hadoop/reducer_3.py
