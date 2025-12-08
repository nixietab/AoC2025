import sys

class DSU:
    def __init__(self,n):
        self.p=list(range(n))
        self.s=[1]*n
        self.c=n
    def f(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]
            x=self.p[x]
        return x
    def u(self,a,b):
        a,b=self.f(a),self.f(b)
        if a==b: return False
        if self.s[a]<self.s[b]: a,b=b,a
        self.p[b]=a
        self.s[a]+=self.s[b]
        self.c-=1
        return True

pts=[tuple(map(int,l.split(','))) for l in open('input.txt') if l.strip()]
n=len(pts)

e=[]
for i in range(n):
    x1,y1,z1=pts[i]
    for j in range(i+1,n):
        x2,y2,z2=pts[j]
        e.append(((x1-x2)**2+(y1-y2)**2+(z1-z2)**2,i,j))
e.sort()

d=DSU(n)
for _,i,j in e[:1000]:
    d.u(i,j)

m={}
for i in range(n):
    r=d.f(i)
    m[r]=m.get(r,0)+1

a=sorted(m.values(),reverse=True)
p1=a[0]*a[1]*a[2]

d=DSU(n)
for _,i,j in e:
    if d.u(i,j) and d.c==1:
        p2=pts[i][0]*pts[j][0]
        break

print(p1)
print(p2)
