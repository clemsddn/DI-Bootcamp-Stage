#Exercice 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionnaire=dict(zip(keys,values))

#Exercice 2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
cout=0
for name , age in family.items():
    if age < 3:
        print(f"{name} votre entré est libre ")
    elif age >=3 and age <= 12 :
        print(f"{name} votre entre coute 10 $ ")
        cout +=10
    elif age >12 :
        print(f"{name} votre entre coute 15 $ ")
        cout +=15
    else :
        pass

print(f"Votre facture s'élève à {cout} $")

family2={}
nb=int(input("Entrez le nombre de personnes :"))
for b in range(nb):
    name=input(f"-Nom {b+1} :")
    age=int(input("Age :"))
    family2[name] = age

cout=0
for name , age in family2.items():
    if age < 3:
        print(f"{name} votre entré est libre ")
    elif age >=3 and age <= 12 :
        print(f"{name} votre entre coute 10 $ ")
        cout +=10
    elif age >12 :
        print(f"{name} votre entre coute 15 $ ")
        cout +=15
    else :
        pass

print(f"Votre facture s'élève à {cout} $")


#Exercice 3
#Question 2
brand={
"name": "Zara" ,
"creation_date": 1975 ,
"creator_name": ["Amancio", "Ortega", "Gaona"] ,
"type_of_clothes": ["men", "women", "children", "home" ],
"international_competitors": ["Gap", "H&M", "Benetton" ],
"number_stores": 7000 ,
"major_color": {
    "France": "blue", 
    "Spain": "red", 
    "US": ["pink", "green"]
        }
    }

#Question 3
brand["number_stores"]=2


#Question 4

print("Les clients de Zara :")
for client in brand["creator_name"]:
    print(client)

#Question 5

brand["country_creation"]="Spain"

#Question 6

for key in brand.keys():
    if key=="international_competitors":
        brand["international_competitors"].append("Desigual")

#Question 7
del brand["creation_date"]

#Question 8

brand["international_competitors"].pop(-1)
#Question 9
print(brand["major_color"]["US"])

#Question 10
print(brand.keys())

#Question 12
more_on_zara ={
    "creation_date": 1975, 
    "number_stores": 10000
}

#Question 13
brand.update(more_on_zara)

#Quetion 14
print(brand["number_stores"])
#update of number_stores value

#Exercice 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

#Question 1
disney_users_A={}
for k in range(len(users)):
    disney_users_A.update({users[k]:k})

print(disney_users_A,"\n\n")

# or

disney_users_A=dict(zip(users,range(len(users))))
print(disney_users_A,"\n\n")

#Question 2
disney_users_B={}
for n in range(len(users)):
    disney_users_B.update({n:users[n]})
print(disney_users_B,"\n\n")
# or

disney_users_B=dict(zip(range(len(users)),users))
print(disney_users_B,"\n\n")

#Question 3
users.sort()
disney_users_C={}
for c in range(len(users)):
    disney_users_C.update({users[c]:c})
print(disney_users_C,"\n\n")

disney_users_C=dict(zip(users,range(len(users))))

print(disney_users_C,"\n\n")

#Question 4
disney_users_A={}
for user in users:
    try:
        b=(list(user)).index("i") 
        
    except:
        b=0
    if not b :
        continue
    users.remove(user)
    
print(users)  

for user in users:
    try:
        b=(list(user)).index("i") 
    except:
        b=0
    if not b :
        continue
    users.remove(user)


for user in users:
    if user[0].lower()=="m" or user[0].lower()=="p":
        users.remove(user)

disney_users_A=dict(zip(users,range(len(users))))
print(disney_users_A,"\n\n")