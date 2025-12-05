def parse(path="input.txt"):
    a, b = open(path).read().strip().split("\n\n")
    ranges = [tuple(map(int, r.split("-"))) for r in a.splitlines()]
    ids    = [int(x) for x in b.splitlines()]
    return ranges, ids

def merged(ranges):
    rs = sorted(ranges)
    out = [rs[0]]
    for a, b in rs[1:]:
        x, y = out[-1]
        if a <= y + 1:
            out[-1] = (x, max(y, b))
        else:
            out.append((a, b))
    return out

def part1(ids, ranges):
    return sum(any(a <= i <= b for a, b in ranges) for i in ids)

def part2(ranges):
    return sum(b - a + 1 for a, b in merged(ranges))

if __name__ == "__main__":
    ranges, ids = parse("input.txt")
    print("Part 1:", part1(ids, ranges))
    print("Part 2:", part2(ranges))
