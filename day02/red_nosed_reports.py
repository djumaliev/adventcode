data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

def is_safe(report):
    diffs = []

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        diffs.append(diff)
    increasing = all(1 <= d <= 3 for d in diffs)
    decreasing = all(-3 <= d <= -1 for d in diffs)
    return increasing or decreasing

safe_count = 0

for line in data.strip().splitlines():
    if line.strip() == "":
        continue

    report = list(map(int, line.split()))
    if is_safe(report):
        safe_count += 1
print(safe_count)
