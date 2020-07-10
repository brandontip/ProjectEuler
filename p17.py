#1-19
undertwent=len('onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneighteen')
undertwent+=len('nineteen')
onenine=len('onetwothreefourfivesixseveneightnine')


#20-99
twenty=6
thirty=6
forty=5
fifty=5
sixty=5
seventy=7
eighty=6
ninety=6

doubledig= undertwent+ 10*46+ 8*onenine
print doubledig

#hundreds
onehundred=10
twohundred=10
threehundred=12
fourhundred=11
fivehundred=11
sixhundred=10
sevenhundred=12
eighthundred=12
ninehundred=11
onethousand=11

total=10*doubledig +110 + 99*(110-11+27)
print total


