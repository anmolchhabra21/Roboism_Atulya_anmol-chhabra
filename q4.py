print("write the string here")
str= input()
lgt= len(str)
for i in range(0,2*lgt,2):
    str= str[:i+1]+str[i]+str[i+1:]
print(str)