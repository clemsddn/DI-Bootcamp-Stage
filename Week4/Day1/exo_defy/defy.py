#importation du module random pour utiliser la methode shuffle
import random as r

#Question 1
chaine = input("Entrer une chaine de 10 caracteres :")
while len(chaine)!=10 :
    if len(chaine)<10:
        print("La chaine est trop courte !\n")
    if len(chaine)>10:
        print("La chaine est trop longue !\n")
    chaine = input("Entrer une chaine de 10 caracteres :")

#Question 2
print(f"\n Le premier caractere est \"{chaine[0]}\" et le dernier caractere est \"{chaine[-1]}\".\n")

#Question 3


for i in range(len(chaine)+1):
    print(f"{chaine[0:i]}\n")

#Question 4
chaine=list(chaine)
r.shuffle(chaine)
chaine="".join(chaine)
print(f"La chaine melangee est : {chaine}\n")