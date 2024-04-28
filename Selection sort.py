n = int(input())
l = list(map(int, input().split()))


fixThis = n - 1
while fixThis > 0:
   maxIndex = fixThis
   for index in range(fixThis):
       if l[index] > l[maxIndex]:
           maxIndex = index
   if maxIndex != fixThis:
       l[maxIndex], l[fixThis] = l[fixThis], l[maxIndex]
   fixThis -= 1
print(*l)
# sample input
# 7
# -2 5 0 8 -3 4 1

#Sample Output 

# -3 -2 0 1 4 5 8
