#monday =0

jan=31
#feb=28
mar=31
apr=30
may=31
june=30
july=31
aug=31
sep=30
oct=31
nov=30
dec=31
year=1900
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

currentday=1

count=0


#year loop
for i in range(0,99):
    feb=28
    year+=i
    #pass through months
    if currentday==6:
        count+=1

    currentday=(currentday +jan)%7
    if currentday==6:
        count+=1

    #feb add 1 accordingly
    if year%4==0:
       if year%100!=0:
           feb+=1
    if year%400==0:
        feb+=1
    currentday=(currentday +feb)%7
    if currentday==6:
        count+=1

    currentday=(currentday +mar)%7
    if currentday==6:
        count+=1

    currentday=(currentday +apr)%7
    if currentday==6:
        count+=1

    currentday=(currentday +may)%7
    if currentday==6:
        count+=1

    currentday=(currentday +june)%7
    if currentday==6:
        count+=1

    currentday=(currentday +july)%7
    if currentday==6:
        count+=1

    currentday=(currentday +aug)%7
    if currentday==6:
        count+=1

    currentday=(currentday +sep)%7
    if currentday==6:
        count+=1

    currentday=(currentday +oct)%7
    if currentday==6:
        count+=1

    currentday=(currentday +nov)%7
    if currentday==6:
        count+=1

    currentday=(currentday +dec)%7


print count




