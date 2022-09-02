
n = int(input())
str = []

for i in range(n):
    str.append(input()) 

uniquelist = []
for letter in str:
    if letter not in uniquelist:
        uniquelist.append(letter)

set(uniquelist)
    
print(len(uniquelist))

for i in (uniquelist):
    print("{} ".format(str.count(i)),end='')