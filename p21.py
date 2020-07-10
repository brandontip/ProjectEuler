def divisors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

totalsum=0


for k in range(2,10000):
    listos=list(divisors(k))
    sum=0
    for i in range(0, len(listos)):
        if listos[i]!=k:
            sum+=listos[i]
    listy=list(divisors(sum))
    sumtwo=0
    for j in range(0, len(listy)):
        if listy[j]!=sum:
            sumtwo+=listy[j]

    if sumtwo==k:
        if sum!=k:
            totalsum+=k

print totalsum
