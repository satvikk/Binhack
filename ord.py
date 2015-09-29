from collections import defaultdict
from collections import OrderedDict
from operator import itemgetter
import itertools
import numpy as np


R  = int(raw_input())
a =[]

for i in xrange(R):
    a.append(raw_input())




for z in range(0,R):

    pns = [''.join(list(k)) for k in itertools.permutations(a[z])]
    dfi = defaultdict(int)
    for ana in pns:
       dfi[ana] += 1
    
    osiri =OrderedDict(sorted(dfi.items())) 
    if len(osiri) == 1:
    	print "no answer"
    	break

    temp = np.array(osiri.keys())
    cindex = np.where(temp == a[z])[0]
    print osiri.keys()[cindex+1]
    #print cindex 
    #in case of Ola Question


    


