lst=[]
y= input()

n=int(input("enter the no. of elements: "))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)


if y=="asc.":
    lst.sort()
    print(lst)
elif y=="dsc.": 
    lst.sort(reverse=True)
    print(lst)
else:
    print(lst)