def maximum_sub_array(arr):
 ans = 0
 sum = 0
 for i in xrange(len(arr)):
   if (sum + arr[i])>0:
     sum += arr[1]
   else :
     sum = 0
   sum = max(sum,ans)
 return ans
