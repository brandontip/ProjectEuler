row1='75'
row2='95 64'
row3='17 47 82'
row20='18 35 87 10'
row4='20 04 82 47 65'
row5='19 01 23 75 03 34'
row6='88 02 77 73 07 63 67'
row7='99 65 04 28 06 16 70 92'
row8='41 41 26 56 83 40 80 70 33'
row9='41 48 72 33 47 32 37 16 94 29'
row10='53 71 44 65 25 43 91 52 97 51 14'
row11='70 11 33 28 77 73 17 78 39 68 17 57'
row12='91 71 52 38 17 14 91 43 58 50 27 29 48'
row13='63 66 04 68 89 53 67 30 73 16 69 87 40 31'
row14='04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

ar1=[int(s) for s in row1.split() if s.isdigit()]
ar2=[int(s) for s in row2.split() if s.isdigit()]
ar3=[int(s) for s in row3.split() if s.isdigit()]
ar20=[int(s) for s in row20.split() if s.isdigit()]
ar4=[int(s) for s in row4.split() if s.isdigit()]
ar5=[int(s) for s in row5.split() if s.isdigit()]
ar6=[int(s) for s in row6.split() if s.isdigit()]
ar7=[int(s) for s in row7.split() if s.isdigit()]
ar8=[int(s) for s in row8.split() if s.isdigit()]
ar9=[int(s) for s in row9.split() if s.isdigit()]
ar10=[int(s) for s in row10.split() if s.isdigit()]
ar11=[int(s) for s in row11.split() if s.isdigit()]
ar12=[int(s) for s in row12.split() if s.isdigit()]
ar13=[int(s) for s in row13.split() if s.isdigit()]
ar14=[int(s) for s in row14.split() if s.isdigit()]

for i in range(0,len(ar13)):
    ar13[i]+=max(ar14[i],ar14[i+1])
for i in range(0,len(ar12)):
    ar12[i]+=max(ar13[i],ar13[i+1])
for i in range(0,len(ar11)):
    ar11[i]+=max(ar12[i],ar12[i+1])
for i in range(0,len(ar10)):
    ar10[i]+=max(ar11[i],ar11[i+1])
for i in range(0,len(ar9)):
    ar9[i]+=max(ar10[i],ar10[i+1])
for i in range(0,len(ar8)):
    ar8[i]+=max(ar9[i],ar9[i+1])
for i in range(0,len(ar7)):
    ar7[i]+=max(ar8[i],ar8[i+1])
for i in range(0,len(ar6)):
    ar6[i]+=max(ar7[i],ar7[i+1])
for i in range(0,len(ar5)):
    ar5[i]+=max(ar6[i],ar6[i+1])
for i in range(0,len(ar4)):
    ar4[i]+=max(ar5[i],ar5[i+1])
for i in range(0,len(ar20)):
    ar20[i]+=max(ar4[i],ar4[i+1])
for i in range(0,len(ar3)):
    ar3[i]+=max(ar20[i],ar20[i+1])
for i in range(0,len(ar2)):
    ar2[i]+=max(ar3[i],ar3[i+1])
for i in range(0,len(ar1)):
    ar1[i]+=max(ar2[i],ar2[i+1])



print ar1