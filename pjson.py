#! /usr/bin/python3
import json
import sys

stdin = ''.join(sys.stdin.readlines())

try:
   json_str = json.loads(stdin)
except Exception as ex:
    raise Exception('Unable to parse stdin, make sure to use JSON only') from ex

print(json.dumps(json_str, indent=4, default=str))

