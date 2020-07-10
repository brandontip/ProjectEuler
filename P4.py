largest="none found"
large=0
for i in range (100, 1000):
    for j in range (100, 1000):
        word = str(i*j)
        current =i*j
        if word==word [::-1]:
            if current > large:
                largest=word
                large= current
print largest
