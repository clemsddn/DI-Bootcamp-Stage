class Family :
    liste=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]
    def __init__(self,last_name,Membres=liste):
        self.last_name=last_name
        self.Membres=Membres
    def born(self,child):
        self.Membres.append(child)
        print(f'Congratulating you are parent !')
    def is_18(self,**kwargs):
        if kwargs['age']>18:
            return 1
        else:
            return 0
    def family_presentation(self):
        print(f' {self.last_name} Familly :')
        for member in self.Membres:
            print(member['name'])
family=Family('DINDANE')
family.family_presentation()

#Exercice 2

class TheIncredibles(Family):
    def use_power(self):
        for member in self.Membres:
            try:
                assert member['age'] >18
                p=member['power']
                n=member['name']
                print(f"\n{n}'s power is {p}")
            except AssertionError:
                n=member['name']
                print(f'\nExecption :{n} not over 18 years old.')
    
    def incredible_presentation(self):
        print(f' {self.last_name} Familly :')
        for member in self.Membres:
            print(member['name'],member['incredible_name'],member['power'])
        super().family_presentation()


liste=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]          

th=TheIncredibles('Dindane',liste)
th.use_power()
th.incredible_presentation()
child={'name':'Jack','age':0,'gender':'Male','is_child':True,'power': 'Unknown Power','incredible_name':'Unknown incredible_name'}

th.born(child)

th.incredible_presentation()