from collections import deque

g = {'A':['B','C'], 'B':['D'], 'C':['E'], 'D':[], 'E':[]}

q = deque(['A'])
v = set(['A'])

while q:
    n = q.popleft()
    print(n, end=' ')
    for i in g[n]:
        if i not in v:
            v.add(i)
            q.append(i)
