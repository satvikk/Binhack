
p, q = map(int, raw_input().strip().split())

a = map(int,raw_input().split(" "))

query2darr = []

for i in xrange(q):
  query2darr.append(map(int,raw_input().split(" ")))

#print a
#print query2darr
val = ans = count = [0]*q


for i in range(0,len(a)):
    for j in range(0,len(query2darr)):
        if a[i]>=query2darr[j][0]:
            count[j]+=1
            if count[j] == query2darr[j][1]:
                ans[j] = a[i]
for i in range(0,q):
	print ans[i]
          
        
