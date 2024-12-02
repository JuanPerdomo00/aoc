def is_safe(row):
    diffs = [row[i + 1] - row[i] for i in range(len(row) - 1)]

    if all(1 <= abs(diff) <= 3 for diff in diffs):
        if all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs):
            return True
    return False


def is_safe_with_one_removal(row):
    for i in range(len(row)):
        new_row = row[:i] + row[i + 1 :]
        if is_safe(new_row):
            return True
    return False


with open("input.txt", "r") as f:
    data = [list(map(int, line.split())) for line in f.readlines()]
safe_count = sum(1 for row in data if is_safe(row) or is_safe_with_one_removal(row))

print(safe_count)
