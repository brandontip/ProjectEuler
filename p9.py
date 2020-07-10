for i in range(0,334):
    for j in range(i,i+334):
        for k in range(j,j+334):
            if i**2+j**2==k**2:
                if i+j+k==1000:
                    print i*j*k