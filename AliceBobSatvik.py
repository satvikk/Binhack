# Enter your code here. Read input from STDIN. Print output to STDOUT
T = map(int, raw_input().strip().split())[0]
n=[]
a=[]
for i in range(0,T):
    n.append( map(int, raw_input().strip().split())[0] )
    a.append( map(int,raw_input().split(" ")) )
for i in range(T):
    if isWinning(a[i]==1):
        print "Alice"
    else:
        print "Bob"
def isSorted(a):
    for i in range(1:len(a)):
        if a[i] <= a[i-1]:
            return 0
    return 1

def isWinning(a):
    if isSorted(a)==1:
        return 1
    for i in range(len(a)):
        b = a[:i] + a[i+1:]
        if isWinning(b)==0:
            return 1