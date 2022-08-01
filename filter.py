# Filter logic in list
runs = [20, 30, 40, 90, 60, 110, 108]
filter = []
for run in runs:
    if run >= 30 and run<=90:
        filter.append(run)
print(filter)