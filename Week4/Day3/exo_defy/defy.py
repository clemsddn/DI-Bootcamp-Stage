"""
##Challenge 1
#Question 1
mot=input("Entrer un mot:")

#Question 2
dic_mot={}
for m in mot:
    liste=[]
    for i in range(len(mot)):
        if m == mot[i]:
            liste.append(i)
        dic_mot.update({m:liste})

for letter, index_liste in dic_mot.items():
    print(f"{letter} : {index_liste} ")
"""

##Defy 2
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1000",
  "Fertilizer": "$20",
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2",
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5000",
  "PC": "$1200"
}

#Question 1
wallet=float(input("Entrer l'argent que vous voulez depensé :"))
produits=[]
for prod in items_purchase.keys():
    if wallet >= float(items_purchase[prod][1:]):
       produits.append(prod)
if produits :
    produits.sort()
    for p in produits:
        print(p)

#Question 2
else:
 print("Nothing : ")