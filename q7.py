print("write the number of elements in the list")
n= int(input())
lt=[]
for i in range(0,n):
    n= int(input())
    lt.append(n)

counter = 0
num = lt[0]
 
for i in lt:
    c_d = lt.count(i)
    if(c_d> counter):
        counter = c_d
        num = i
print("the highest frequency element in the array is:")
print(num)