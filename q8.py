x = input()
n= len(x)
sum=0
for i in range(0,n):
    if(x[i].isdigit()==True):
        sum= sum+int(x[i])
print(sum)