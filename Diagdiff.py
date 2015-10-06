# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
a=[]
sum=0
for i in range(n):
    a.append( map(int,raw_input().split()))
for i in range(n):
    sum+=a[i][i]-a[n-i-1][i]

print abs(sum)