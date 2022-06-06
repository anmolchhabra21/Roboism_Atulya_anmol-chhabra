print("write your credit card number here!")
credc= input()
n= len(credc)
print(n)
for i in range(0,n-4):
    credc=credc.replace(credc[i],'*',1)
print(credc)