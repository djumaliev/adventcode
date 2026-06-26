def is_safe(report):
    diffs = []

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        diffs.append(diff)
    increasing = all(1 <= d <= 3 for d in diffs)
    decreasing = all(-3 <= d <= -1 for d in diffs)
    return increasing or decreasing

safe_count = 0

with open("example.txt") as file:
    for line in file:
        if line.strip() == "":
            continue

        report = list(map(int, line.split()))

        if is_safe(report):
            safe_count += 1

print(safe_count)
