#My code can find the only repeated number out of any number n as it would be more useful so we have to give it an input as 100 for finding the value
print("write the no. of elements in the array")
n= int(input())
orgsum= n*(n-1)/2
lst=[]
for i in range(0,n):
    x= input()
    lst.append(x)
sum=0
for i in range(0,n):
    sum= int(sum)+int(lst[i])
print(int(sum-orgsum))