p, q = map(int, raw_input().strip().split())

a = map(int,raw_input().split(" "))

query2darr = []

for i in xrange(q):
  query2darr.append(map(int,raw_input().split(" ")))

#print a
#print query2darr
count = [0,0,0,0]
val = [ 0 , 0, 0, 0]

#change l and a ccordingly,you can use debug prints

for i in range(0,len(a)):
    for j in range(0,len(l)):
        if a[i]>=l[j]:
            count[j]+=1
            if count[j] == k[j]:
                print a[i]
          
        
