#print all duplicates in a list

list = [1,2,3,3,4,5,2,1]


dict = {}

# for s in list:
#     dict.update({s:0})

for x in list:
    dict.update({x:dict[x]+1})

print(dict)


j=[k for (k,v) in dict.items() if v>1]

print(j)
