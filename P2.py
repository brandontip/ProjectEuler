first=1
second=1
sum=0
while (second < 4000000):
    dummy=second
    second += first
    if second%2==0:
        sum+= second
    first=dummy

print sum