import numpy as np
p, q = map(int, raw_input().strip().split())

a = map(int,raw_input().split(" "))

query2darr = []

for i in xrange(q):
  query2darr.append(map(int,raw_input().split(" ")))

cortana = []

for i in a:
 cortana.append([i,[],i])

print cortana
print query2darr



for L,R in query2darr:
   print "////////////////////////////////////////////////////////////////////////////////////////////////////////////////",L,R
   mincounter = []
   cortana[L-1][1].append(R-1)
   cortana[R-1][1].append(L-1)
   print "aaaaaaaaaaaaaaaaaaaaaaaapppppppppppppend",cortana
   cortana[L-1][2] += cortana[R-1][0]  
   cortana[R-1][2] = cortana[L-1][2]
   print "On CONNNNNNNNNNNNNNNNECT LLLLLequal",cortana
   if len(cortana[L-1][1]) > len(cortana[R-1][1]):
     for ind in cortana[L-1][1]:
       cortana[ind][2] = cortana[L-1][2]
       print "invariant L>R",cortana
   else:
     for ind in cortana[R-1][1]:
       cortana[ind][2] = cortana[R-1][2]
       print "invariant R>L",cortana
   for z in xrange(len(cortana)):
     mincounter.append(cortana[z][2])     
     minindex = np.argmin(mincounter)
     print "mincccccccccccccccounter",mincounter
   print "AAAAAAAAAAAAAAAAAAAAAAAAAAANNNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSSSSSSS",mincounter[minindex]
