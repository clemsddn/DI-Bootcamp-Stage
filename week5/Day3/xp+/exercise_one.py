import random as r
import string as s
import datetime as dt

#Exercice 1
import func
func.addition(5,10)

#Exercice 2
def aleatoire():
    x=0
    a=r.randint(1,100)
    try:
      nb=int(input("Enter a integer number between 1 and 100 :"))
    except:
        nb=int(input("Enter a integer number between 1 and 100 :"))

    while a!=nb:
        if nb<a:
            print("it is great")
        else:
            print("it is small ")
        try:
            nb=int(input("Enter a integer number between 1 and 100 :"))
        except:
            nb=int(input("Enter a integer number between 1 and 100 :"))
    else:
        print(f"Congratulation !")  
aleatoire()
#Exercice 3
def stringGenerator():
    chaine=list(s.ascii_letters)
    res=''
    for i in range(5):
        res+=r.choice(chaine)
    return res
    
print(stringGenerator())

#Exercice 4
x=dt.datetime.now()
print(f"Today date is :{x}")

#Exercice 5
y=dt.datetime.now()
x=dt.datetime(2023,2,1,10,34,1)
print(f"Le temps restant d'ici le 1er fevrier:{x-y}")