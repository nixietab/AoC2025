#!/usr/bin/env python3
import sys
from collections import defaultdict

def read_grid(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f if line.rstrip("\n") != ""]
    w = max(len(l) for l in lines)
    return [list(l.ljust(w, ".")) for l in lines]

def find_start(grid):
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                return r, c
    raise SystemExit("No S found")

# ---------- Part 1 ----------
def count_classical_splits(grid):
    rows, cols = len(grid), len(grid[0])
    sr, sc = find_start(grid)

    beams = {sc}
    splits = 0

    for r in range(sr + 1, rows):
        next_beams = set()
        for c in beams:
            if not (0 <= c < cols):
                continue
            if grid[r][c] == "^":
                splits += 1
                next_beams |= {c - 1, c + 1}
            else:
                next_beams.add(c)
        beams = next_beams
        if not beams:
            break

    return splits

# ---------- Part 2 ----------
def count_quantum_timelines(grid):
    rows, cols = len(grid), len(grid[0])
    sr, sc = find_start(grid)

    # dp[col] = number of timelines reaching this column at current row
    dp = defaultdict(int)
    dp[sc] = 1

    for r in range(sr + 1, rows):
        nxt = defaultdict(int)
        for c, ways in dp.items():
            if not (0 <= c < cols):
                continue
            if grid[r][c] == "^":
                nxt[c - 1] += ways
                nxt[c + 1] += ways
            else:
                nxt[c] += ways
        dp = nxt
        if not dp:
            break

    # every surviving path is a distinct timeline
    return sum(dp.values())

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    grid = read_grid(path)

    p1 = count_classical_splits(grid)
    p2 = count_quantum_timelines(grid)

    print(f"Part 1 (classical splits): {p1}")
    print(f"Part 2 (quantum timelines): {p2}")

if __name__ == "__main__":
    main()
