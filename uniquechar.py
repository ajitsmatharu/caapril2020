#find unique characters in a string

string = input('Enter string\n') #input the string

charset = set(string) #make a set from characters of the string
dict = {} #create empty dict

for j in charset:

    dict.update({j:0}) #fill dict with keys of unique characters

for j in string:

    dict[j]+=1 #increment values by 1 for each char in string

print(dict)
