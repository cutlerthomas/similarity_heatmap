#!/bin/python3

import sys
import json

for line in sys.stdin:
    line = line.strip()
    if line:
        source, content = line.split(":::", 1)
        print(json.dumps({"source": source, "content": content}))
