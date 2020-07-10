longestlength=1
longestnumber=1
for i in range(1,1000001):
    count=1
    current=i
    while current !=1:
        if current%2==0:
            current*=.5
        else:
            current=3*current +1
        count+=1
    if count > longestlength:
        longestlength= count
        longestnumber=i
    if i%10000==0:
        print 'i/10000' + 'percent done'
print longestnumber