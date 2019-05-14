


#assign a variable to this word,'kakorrhaphiophobia'.
#determine length using len, then for loop it to determine length.  print both results
#count each vowel separately, print results
#for loop the count with and if-elif-else, print results again


##Preliminary Variables
##Input
##Processing
##Output


##Preliminary Variables
##Input
wth = 'kakorrhaphiophobia'
print('Here is my word,',wth,',stored in a variable.')
##Output
print('The word is',len(wth),'characters long.')
j = len(wth)
##Output

count = 0
for taco in wth:
    count = count + 1
    print(count)##Processing
print('Looking at it another way, the word is still',j,'characters long.')
##Output
##Preliminary Variables
a = wth.count('a')
e = wth.count('e')##Processing
i = wth.count('i')
o = wth.count('o')
u = wth.count('u')
sometimesY = wth.count('y')
print("The vowels present and counted in the word are; A's",a,"E's",e,"I's",i,"O's",o,"U's",u,"Y's",sometimesY)
##Output
##Preliminary Variables
aa = 0
ee = 0
ii = 0
oo = 0
uu = 0
con = 0

for burito in wth:
    if burito == 'a':
        aa = aa + 1
    elif burito == 'e':
        ee = ee + 1
    elif burito == 'i':##Processing
        ii = ii + 1
    elif burito == 'o':
        oo = oo + 1
    elif burito == 'u':
        uu = uu + 1
    else:
        burito != 'a' or burito != 'e' or burito != 'i' or burito != 'o' or burito != 'u'
        con = con +1
       
print(aa,"That is the total number of A's")
print(ee,"That is the total number of E's")
print(ii,"That is the total number of I's")
print(oo,"That is the total number of O's")##Output
print(uu,"That is the total number of U's")
print('Your running total of consonants so far is;',con,'in case you were wondering.')
