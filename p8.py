numberone= '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254'
numbertwo= '69874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493'
numberthree='3589072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243525849'
numberfour='771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637'
numberfive= '484403199890008895243450658541227588666881164271714799244429282308634656748139191231628245861786645835912456652947654568284891288314260769'
numbersix= '42242190226710556263211111093705442175069416589604080719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606'
numberseven= '58861164671094050775410022569831552000559357297257163626956188267042825248360082325753042075296345'
lengthone=len(numberone)
lengthtwo=len(numbertwo)
lengththree=len(numberthree)
lengthfour=len(numberfour)
lengthfive=len(numberfive)
lengthsix=len(numbersix)
lengthseven=len(numberseven)
largestproduct=0

for i in range(0,lengthone-13):
    test=1
    for j in range(0,13):
        test*= int(numberone[i+j])
    print test
    if test > largestproduct:
        largestproduct=test
for i in range(0,lengthtwo-13):
    test=1
    for j in range (0,13):
        test*=int(numbertwo[i+j])
    if test > largestproduct:
        largestproduct=test
for i in range(0,lengththree-13):
    test=1
    for j in range (0,13):
        test*=int(numberthree[i+j])
    if test > largestproduct:
        largestproduct=test
for i in range(0,lengthfour-13):
    test=1
    for j in range (0,13):
        test*=int(numberfour[i+j])
    if test > largestproduct:
        largestproduct=test
for i in range(0,lengthfive-13):
    test=1
    for j in range (0,13):
        test*=int(numberfive[i+j])
    if test > largestproduct:
        largestproduct=test
for i in range(0,lengthsix-13):
    test=1
    for j in range (0,13):
        test*=int(numbersix[i+j])
    if test > largestproduct:
        largestproduct=test
for i in range(0,lengthseven-13):
    test=1
    for j in range (0,13):
        test*=int(numberseven[i+j])
    if test > largestproduct:
        largestproduct=test
print largestproduct
print lengthone



