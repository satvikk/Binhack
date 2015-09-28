# Enter your code here. Read input from STDIN. Print output to STDOUT


a = []
t = int(raw_input())
for k in range(t):
    N, M = map(int, raw_input().strip().split())
    a.append(map(int,raw_input().split(" ")))


def maximum_sub_array(arr,M):
 ans = 0
 sum = 0
 for i in xrange(len(arr)):
   if ((sum + arr[i]) % M) - (sum % M) > 0:
     sum += arr[1]
   else :
     sum = 0
   ans = max(sum,ans)
 return ans
    
    
    
for i in a:
  print maximum_sub_array(i,M)%M
    
