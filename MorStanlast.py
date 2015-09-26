import numpy as np

p, q = map(int, raw_input().strip().split())

a = map(int,raw_input().split(" "))

query2darr = []

for i in xrange(q):
  query2darr.append(map(int,raw_input().split(" ")))

#print a
#print query2darr


#change l and a ccordingly,you can use debug prints

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
