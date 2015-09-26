# Enter your code here. Read input from STDIN. Print output to STDOUT
n, qn = map(int, raw_input().strip().split())

w = map(int,raw_input().split(" "))
q=[]
for i in xrange(qn):
  q.append(map(int,raw_input().split(" ")))

adr=[]
for i in range(0,qn):
    adr.append(i)
for i in range(0,qn):
    if adr[ q[i][0] -1] == adr[ q[i][1] -1]:
        continue
    w[ q[i][0] -1 ] += w[ q[i][1] -1]
    w[ q[i][1] -1 ] =  w[ q[i][0] -1]
    if adr[q[i][1] -1 ]>adr[q[i][0] -1]: 
        for j in range(0,n):
            if adr[ q[j][1] -1] == adr[ q[i][1] -1]:
             adr[ q[j][1] -1 ] = adr[ q[i][0] -1]
             w[ q[j][1] -1 ] = w[ q[i][0] -1]
    else:
        for j in range(0,n):
            if adr[ q[j][0] -1] == adr[ q[i][0] -1]:
             adr[ q[j][0] -1 ] = adr[ q[i][1] -1]
             w[ q[j][0] -1 ] = w[ q[i][1] -1]
    print min(w)
    
    