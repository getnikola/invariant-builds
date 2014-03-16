#!/usr/bin/env python
# For internal use only.
"""Return data from the build data file."""
import sys
try:
    a = sys.argv[1]
except:
    print('no value specified')
    exit(1)

with open('BUILD-DATA') as fh:
    pairs = [l.strip() for l in fh.readlines()]

data = {}

for pair in pairs:
    k, v = pair.split(':')
    k = k.strip()
    v = v.strip()
    data[k] = v

print(data[a])
