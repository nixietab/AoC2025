# Day 2 AoC2025

def parse_ranges(s: str):
    return [tuple(map(int, p.split("-")))
            for p in s.replace(" ", "").split(",") if p]

def repeated_exactly_twice(n: int) -> bool:
    s = str(n)
    mid = len(s) // 2
    return len(s) % 2 == 0 and s[:mid] == s[mid:]

def repeated_at_least_twice(n: int) -> bool:
    s = str(n)
    L = len(s)
    for k in range(1, L // 2 + 1):
        if L % k == 0 and s == s[:k] * (L // k):
            return True
    return False

def solve(filename: str):
    with open(filename) as f:
        ranges = parse_ranges(f.read().strip())

    part1 = part2 = 0

    for a, b in ranges:
        for n in range(a, b + 1):
            if repeated_exactly_twice(n):
                part1 += n
            if repeated_at_least_twice(n):
                part2 += n

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == "__main__":
    solve("input.txt")