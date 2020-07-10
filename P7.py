counter =2
number=3
while counter < 10001:
    number+=2
    prime=1
    if number%4==1 or number%4==3:
        for j in range (2,int(number**.5)+1):
            if number%j==0:
                prime=0
    else:
        prime=0
    if prime==1:
        counter+=1
print number