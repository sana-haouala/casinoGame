import os
from random import randrange
from math import ceil
num=input("un num : ")
num= int(num)
if num%2==0:
 couleurN="noir"
else:
 couleurN="rouge" 
somme = input("Preciser le somme dont tu veux desirer jouer: ")
somme= int(somme)
numR=randrange(50)
print("la roulette s'arrete sur ",numR)
if numR%2==0:
 couleurR="noir"
else:
 couleurR="rouge"
if num==numR:
 somme+=somme*3
 print("vous avez gagner 3 fois votre somme",somme) 
else:
 if couleurN==couleurR:
   somme+=ceil(somme/2)
   print("vous avez gagner 50% de plus,votre somme devient: ",somme) 
 else:
    print("vous avez perdu :/")
os.system("pause")
	

