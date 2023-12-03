#!/usr/bin/env python3

import json
import csv

with open('results/results.json', 'r') as f:
    data = json.load(f)

# extract columns from each dictionary
extracted = []
for item in data:
    row = [
        item.get("type", ""),
        item.get("module", ""),
        item.get("path", ""),
        item.get("symbol", ""),
        item.get("message", ""),
        item.get("message-id", "")
    ]
    extracted.append(row)

# create csv file
with open('pylint_extract.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # header row with column names
    csv_writer.writerow(["type", "module", "path", "symbol", "message", "message-id"])
    csv_writer.writerows(extracted)

