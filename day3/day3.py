def k(s,n):
    o=[];d=len(s:=s.strip())-n
    for c in s:
        while d and o and o[-1]<c:o.pop();d-=1
        o+=c
    return int(''.join(o[:n]))

L=[l.strip()for l in open("input.txt")if l.strip()]
print(sum(k(l,2)for l in L),sum(k(l,12)for l in L))