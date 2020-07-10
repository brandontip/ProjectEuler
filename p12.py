
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
found=False
current=1
while found==False:
    current+=1
    numberoffactors=len(factors(int(.5*(current)*(current+1))))
    if numberoffactors>350:
        print "close"
    if numberoffactors>500:
        print    int(.5*(current)*(current+1))
