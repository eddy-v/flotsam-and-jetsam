# eddy vasile
# how to check validity of bank routing number (aba)
# multiply the first 8 digits with the sequence 3, 7, 1, 3, 7, 1, 3, 7 and add the results
# the largest multiple of 10 of the sum calculated above must be equal to the 9th digit (checkDigit)
import math
def validateABA(aba):
    checkDigit=int(aba[8])
    digitSum= \
    int(aba[0])*3+ \
    int(aba[1])*7+ \
    int(aba[2])+   \
    int(aba[3])*3+ \
    int(aba[4])*7+ \
    int(aba[5])+   \
    int(aba[6])*3+ \
    int(aba[7])*7
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
