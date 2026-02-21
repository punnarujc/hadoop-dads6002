#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    # Parse the input from mapper
    try:
        person, district, income = line.split('\t')
        income = float(income)
    except ValueError:
        # If line is malformed, skip it
        continue

    print("{}\t{}\t{}".format(person, district, income))
