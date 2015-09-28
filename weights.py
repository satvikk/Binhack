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
    x,y = q[i][0] -1 ,  q[i][1] -1
    if adr[x] == adr[y]:
        print min(w)
        continue
    ad = sorted([adr[x],adr[y]])
    w[ad[0]] = w[adr[x]-1]+w[adr[y]]
    for j in range(0,n):
        if adr[j] == ad[1]:
            adr[j] = ad[0]
        if adr[j] == ad[0]:
            #w[j] = w[ad[0]]
            
    
    
    print min(w)
    #print w
    #print adr
