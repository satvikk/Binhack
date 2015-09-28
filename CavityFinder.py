import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = map(int, raw_input().strip().split())[0]
a=[]
b=[]
for i in range(0,n):
    b.append( map(int, raw_input().strip().split())[0] )
    a.append(map(int, str(b[i])))  
for i in range(1,n-1):
    for j in range(1,n-1):
        if a[i][j]>a[i+1][j] and a[i][j]>a[i-1][j] and a[i][j]>a[i][j+1] and a[i][j]>a[i][j-1]:
            a[i][j]='X'
for i in range(0,n):
    for j in range(n):
        if j==n-1:
            print a[i][j]
        else:
            sys.stdout.write(str(a[i][j]))