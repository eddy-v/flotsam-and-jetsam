# eddy@eddyvasile.us
# how to check validity of bank routing number (aba)
# multiply the first 8 digits with the sequence 3, 7, 1, 3, 7, 1, 3, 7 and add the results
# the largest multiple of 10 of the sum calculated above must be equal to the 9th digit (checkDigit)
import math
def validateABA(aba):
    factor=[3,7,1,3,7,1,3,7]
    checkDigit=int(aba[8])
    digitSum=0
    for i in factor:
        digitSum=digitSum+int(aba[i])*factor[i]
    if digitSum==0:
        digitSum=10
#For a more elegant soution use lists or arrays
#Find the highest multiple of 10 of the digitSum
    temp = (math.floor(digitSum/10)*10)+10;
    validDigit=temp-digitSum;        
    if validDigit==checkDigit:
        return True
    else:
        return False   
aba=input("Enter the 9 didigit bank routing nuber (e.g. 121000248): ")
if aba.isalpha() or len(aba) != 9:
   print ('Sorry... 9 digit numeric input required\n')
else:
    if (validateABA(aba)):
        print(aba,' is a valid bank routing number\n')
    else:
        print(aba,' is NOT a valid routing number\n')
