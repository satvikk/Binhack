def maximum_sub_array(arr):
 ans = 0
 sum = 0
 for i in xrange(len(arr)):
   if (sum + arr[i])>0:
     sum += arr[1]
   else :
     sum = 0
   ans = max(sum,ans)
 return ans


def mssl(l):
    best = cur = 0
    for i in l:
        cur = max(cur + i, 0)
        best = max(best, cur)
    return best







def maxsumNonContiguous(array){
     sum1 = array[0]
     sum2 = 0;
     for i in array:
         sum3 = Math.max(sum1,sum2)
         sum1 = sum2 + array[i]
         sum2 = sum3
     return max(sum1, sum2);
 


"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
def maxsumNonContiguous(array):
   sum1 = array[0]
   sum2 = 0;
   for i in range(1,len(array)):
      sum3 = max(sum1,sum2)
      sum1 = sum2 + array[i]
      sum2 = sum3
   return max(sum1, sum2);

def maximum_sub_array(arr):
 ans = 0
 sum = 0
 for i in xrange(len(arr)):
   if (sum + arr[i])>0:
     sum += arr[1]
   else :
     sum = 0
   ans = max(sum,ans)
 return ans

a = []
t = int(raw_input())
for k in range(t):
    N = int(raw_input())
    a.append(map(int,raw_input().split(" ")))
    
for i in a:
    print maxsumNonContiguous(i),maximum_sub_array(i)

"""
