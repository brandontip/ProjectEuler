num='93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827'
num2='223758251185210916864'

sum=0

arr=[int(s) for s in num.split() if s.isdigit()]
for i in range(0,len(num)):
    sum+=int(num[i])

for i in range(0,len(num2)):
    sum+=int(num2[i])

print sum
