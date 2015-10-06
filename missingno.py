# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
a = map(int,raw_input().split())
m = int(raw_input())
b =map(int,raw_input().split())
a1=[0]*101
b1=[0]*101
mini = min(b)
for i in range(len(b)):
    if i<len(a):
        a1[(a[i]-mini)%101]+=1
    b1[(b[i]-mini)%101]+=1
ans=[]
for i in range(101):
    if a1[i]<b1[i]:
        ans.append(i+mini)
for i in range(len(ans)):
    print ans[i],