import math
largest=1
for i in range(1, int(600851475143**.5)):
    if 600851475143%i==0:
        print "made it"
        prime=1
        if i%4==1 or i%4==3:
            for j in range (2,int(i**.5)):
                if i%j==0:
                    prime=0
        else:
            prime=0
        if prime==1:
            largest=i

print largest


