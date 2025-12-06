from functools import reduce
import operator

def product(it):
    return reduce(operator.mul, it, 1)

lines = [l.rstrip("\n") for l in open("input.txt")]
h = len(lines)
w = max(len(l) for l in lines)
p = [l.ljust(w) for l in lines]

sep = [all(r[c] == " " for r in p) for c in range(w)]

blocks = []
c = 0
while c < w:
    if sep[c]:
        c += 1
    else:
        s = c
        while c < w and not sep[c]:
            c += 1
        blocks.append((s, c - 1))

def find_op(s, e):
    for r in range(h - 1, -1, -1):
        for ch in p[r][s:e + 1]:
            if ch in "+*":
                return ch
    return "+"

def eval_p1(s, e):
    items = []
    for r in range(h):
        seg = p[r][s:e + 1].strip()
        if not seg:
            continue
        op = "".join(ch for ch in seg if ch in "+*")
        num = "".join(ch for ch in seg if ch.isdigit() or ch == "-")
        if num:
            items.append(int(num))
        if op:
            return sum(items) if op == "+" else product(items)
    return 0

def eval_p2(s, e):
    op = find_op(s, e)
    nums = []
    for c in range(e, s - 1, -1):
        digits = "".join(p[r][c] for r in range(h - 1) if p[r][c] != " ")
        if digits:
            nums.append(int(digits))
    return sum(nums) if op == "+" else product(nums)

print(sum(eval_p1(s, e) for s, e in blocks))
print(sum(eval_p2(s, e) for s, e in blocks))
