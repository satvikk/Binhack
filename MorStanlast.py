p = 10
q = 4
a = [1, 9, 2 ,8, 3, 7, 4, 6, 5, 10]
l = [4,3,1,8]
k = [4,2,6,1]
count = [0,0,0,0]
val = [ 0 , 0, 0, 0]
for i in range(0,len(a)):
    for j in range(0,len(l)):
        if a[i]>=l[j]:
            count[j]+=1
            if count[j] == k[j]:
                print a[i]
          
        