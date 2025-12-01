# Day 1 AoC 2025
def load_rotations():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]

def part1(rotations):
    pos = 50
    hits = 0

    for line in rotations:
        direction = line[0]
        dist = int(line[1:])

        if direction == 'L':
            pos = (pos - dist) % 100
        else:
            pos = (pos + dist) % 100

        if pos == 0:
            hits += 1

    return hits


def part2(rotations):
    pos = 50
    hits = 0

    for line in rotations:
        direction = line[0]
        dist = int(line[1:])
        step = -1 if direction == "L" else +1

        for _ in range(dist):
            pos = (pos + step) % 100
            if pos == 0:
                hits += 1

    return hits

rotations = load_rotations()

print("Code 1:", part1(rotations))
print("Code 2:", part2(rotations))
