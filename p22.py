from string import ascii_uppercase


fil=open('p22names')

str=fil.read().split(',')

#sort alphabetically
str.sort()


#takes in a string of all capitals and returns the "word score", the sum of its letters A=1, B=2, etc
def score(word):
    return sum(ascii_uppercase.index(c)+1 for c in word.strip('"'))

#enum turns list into "set" up tuples
#1 means start enumeration at 1
print sum(i*score(x) for i,x in enumerate(str,1))


