<<<<<<< HEAD
=======
import numpy as np
>>>>>>> 922351ca7aefc54224e32d48dc829e3a29ed13d9

p, q = map(int, raw_input().strip().split())

a = map(int,raw_input().split(" "))

query2darr = []

for i in xrange(q):
  query2darr.append(map(int,raw_input().split(" ")))

#print a
#print query2darr
<<<<<<< HEAD
val = ans = count = [0]*q
=======

>>>>>>> 922351ca7aefc54224e32d48dc829e3a29ed13d9


<<<<<<< HEAD
for i in range(0,len(a)):
    for j in range(0,len(query2darr)):
        if a[i]>=query2darr[j][0]:
            count[j]+=1
            if count[j] == query2darr[j][1]:
                ans[j] = a[i]
for i in range(0,q):
	print ans[i]
          
        
=======
maxindex = np.argmax(a)
max = a[maxindex]
cortana = [0]*(max+1)
for i in a:
  cortana[i] += 1
  


def cortanamax(query2darr,cortana):
  print query2darr,cortana
  sum = 0
  for L,K in query2darr:
    print L,K
    for pitr in xrange(L,len(cortana)):
      print pitr
      sum = sum + cortana[L]
      print "after summmmmmmmming",sum
      if sum == K:
       return pitr
    
cortanamax(query2darr,cortana)
>>>>>>> 922351ca7aefc54224e32d48dc829e3a29ed13d9
