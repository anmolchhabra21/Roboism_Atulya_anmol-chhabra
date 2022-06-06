print("write the string here to be checked")
x= input()
n= len(x)
flag=0
for i in range(0,int(n/2)):
    if(x[i]!=x[n-i-1]):
        flag=1
        break
if(flag==1):
    print("this is not a palindrome")
else: print("this is a palidrome")