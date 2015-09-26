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
   if cortana[L-1][2] != cortana[R-1][2]:
      print "////////////////////////////////////////////////////////////////////////////////////////////////////////////////",L,R
      mincounter = []
      cortana[L-1][1].append(R-1)
      cortana[R-1][1].append(L-1)
      print "aaaaaaaaaaaaaaaaaaaaaaaapppppppppppppend",cortana
      cortana[L-1][2] += cortana[R-1][2]  
      cortana[R-1][2] = cortana[L-1][2]
      print "On CONNNNNNNNNNNNNNNNECT LLLLLequal",cortana

      for ind in cortana[L-1][1]:
          print "iiiiiiiiiiiiiinnnnnnnnnnnnndddddddddd",ind
          cortana[ind][2] = cortana[L-1][2]
          for ajax in cortana[ind][1]:
            cortana[ajax][2] = cortana[L-1][2]
          print "invar Checking L-1 conn",cortana

      for inda in cortana[R-1][1]:
          print "iiiiiiiiiiiiiiiiinnnnd",inda
          cortana[inda][2] = cortana[R-1][2]

          for ajaxa in cortana[ind][1]:
            cortana[ajaxa][2] = cortana[L-1][2]
          print "invariant R>L",cortana

      for z in xrange(len(cortana)):
        mincounter.append(cortana[z][2])     
        minindex = np.argmin(mincounter)
        print "mincccccccccccccccounter",mincounter
        print "AAAAAAAAAAAAAAAAAAAAAAAAAAANNNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSSSSSSS",mincounter[minindex]
