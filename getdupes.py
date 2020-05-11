#print all duplicates in a list

list = list(input('Enter list'))

set = (set(list)) #1,2,3,4,5

dict = {}

for s in set:
    dict.update({s:0})

for x in list:
    dict.update({x:dict[x]+1})

j=[k for (k,v) in dict.items() if v>1]

print(j)
