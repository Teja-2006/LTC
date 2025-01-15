##      LINEAR SEARCH
##  this is the most unefficient way to write this program

n = input("What is the size of the array?")
m = int(n)
print("Enter the elements of the array")
arr=[]
i = m
while(i != 0):
   a = int(input())
   arr.append(a)
   i-=1
s = int(input("Enter the element to be searched"))
loc = -1
# Linear search
for i in range(m):
    if arr[i] == s:
        loc = i
    else:
        continue
i+=1
if loc>=0:
    print(f"the location of {s} is : {loc}")
else:
    print("something went wrong")
    
        
