g = [list(l.strip()) for l in open("input.txt") if l.strip()]
H = len(g)
W = max(len(r) for r in g)
for r in g:
    r += ['.'] * (W - len(r))

D = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def neighbors(G, i, j):
    return sum(
        0 <= i+dr < H and 0 <= j+dc < W and G[i+dr][j+dc] == '@'
        for dr, dc in D
    )

part1 = sum(
    g[i][j] == '@' and neighbors(g, i, j) < 4
    for i in range(H)
    for j in range(W)
)

G = [row[:] for row in g]
removed = 0

while True:
    batch = [
        (i, j)
        for i in range(H)
        for j in range(W)
        if G[i][j] == '@' and neighbors(G, i, j) < 4
    ]
    if not batch:
        break
    removed += len(batch)
    for i, j in batch:
        G[i][j] = '.'

print("Part 1:", part1)
print("Part 2:", removed)
