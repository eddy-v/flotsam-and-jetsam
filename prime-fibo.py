#calc prime fibonacci nums
from math import sqrt; from itertools import count, islice
 
def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
 
a,b = 1,1
n=int(input("Enter max: "))
for i in range(n-1):
  a,b = b,a+b
#  print(a)
  if isPrime(a):
    print(a)
    
