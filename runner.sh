#!/bin/bash
rm -r articles
../../hadoop-3.3.6/bin/hadoop jar ../../hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -mapper mapper.py -reducer reducer.py -input part-00000 -output articles