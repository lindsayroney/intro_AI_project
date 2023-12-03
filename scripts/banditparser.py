#!/usr/bin/env python3

import json
import csv

# Read the JSON data from the file
with open('results/bandit.json', 'r') as f:
    data = json.load(f)

# extract columns from the "results" key
results = data.get("results", [])

# extract columns from each dictionary in the "results" list
extracted = []
for item in results:
    issue_cwe_dict = item.get("issue_cwe", {})
    issue_cwe_id = issue_cwe_dict.get("id", "")
    row = [
        item.get("filename", ""),
        issue_cwe_id,
        item.get("issue_text", ""),
        item.get("issue_severity", ""),
        item.get("test_id", ""),
        item.get("test_name", "")
    ]
    extracted.append(row)

# create CSV file
with open('bandit_extract.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # header row with column names
    csv_writer.writerow(["Filename", "issue_cwe_id", "issue_text", "issue_severity", "test_id", "test_name"])
    csv_writer.writerows(extracted)

