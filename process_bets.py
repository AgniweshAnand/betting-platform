import csv

SOURCE_CSV = "sports_betting_predictive_analysis.csv"
TARGET_CSV = "custom_bets.csv"

with open(SOURCE_CSV, mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    print("Detected columns in original CSV:", reader.fieldnames)
    
    first_10_rows = []
    for i, row in enumerate(reader):
        if i >= 10:
            break
        first_10_rows.append(row)

target_headers = ["s.no"] + reader.fieldnames

with open(TARGET_CSV, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=target_headers)
    writer.writeheader()  
    
    for idx, row in enumerate(first_10_rows, start=1):
        row["s.no"] = idx
        writer.writerow(row)

print(f"Success! Created {TARGET_CSV} with proper column headers and 50 rows.")


import random

rand_uniform = round(random.uniform(10.5, 50.5), 1)

rand_list = [round(random.uniform(10.5, 50.5), 1) for _ in range(5)]

print("Single value:", rand_uniform)
print("List of values:", rand_list)