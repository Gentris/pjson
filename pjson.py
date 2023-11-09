#!/usr/bin/python3

import ast
import json
import sys

stdin: str = "".join(sys.stdin.readlines())
try:
    parsed = ast.literal_eval(stdin)
except ValueError:
    parsed = str(stdin)
stdout: str = json.dumps(parsed, indent=4, default=str)

print(stdout)
