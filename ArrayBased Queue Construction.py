Q = []
n = int(input().strip())
while n > 0:
   word = list(map(int, input().split()))
   l = word[0]
   if l == 1:
       num = word[1]
       Q.append(num)
       print(num, "inserted")
   elif l == 2:
       if len(Q) == 0:
           print("Queue is empty")
       else:
           print(Q[0])
   elif l == 3:
       if len(Q) == 0:
           print("Queue is empty")
       else:
           print(Q[0])
           Q.pop(0)
   elif l == 4:
       if len(Q) == 0:
           print("Queue is empty")
       else:
           for ele in Q:
               print(ele, end = " ")
           print()
   else:
       if len(Q) == 0:
           print("Queue is empty")
       else:
           print("Queue is not empty")
      
   n -= 1
#sample input
# 11
# 1 12
# 1 34
# 1 56
# 1 32
# 2
# 4
# 3
# 4
# 5
# 1 222
# 4
#Sample Output 

# 12 inserted
# 34 inserted
# 56 inserted
# 32 inserted
# 12
# 12 34 56 32
# 12
# 34 56 32
# Queue is not empty
# 222 inserted
# 34 56 32 222

