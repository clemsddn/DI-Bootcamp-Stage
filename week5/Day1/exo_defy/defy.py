class Farm:
    def __init__(self,labelle):
        self.labelle=labelle
        self.registre={}
        print(f"\n{self.labelle}'s farm.")
    def add_animal(self,name,nb=1):
        self.name=name
        if self.name  in self.registre.keys():
                self.registre[self.name] +=nb
        else:
            self.registre[self.name] =nb

    def get_info(self):
        for i,j in self.registre.items():
            print( f"\n{i} : {j}")
        print('     E-I-E-I-0!')
    
    def get_animal_types(self): 
        res = list(self.registre.keys())
        chaine=", ".join(res[0:len(res)-1])
        return f'{chaine} and {res[-1]}'
    def Farmget_short_info(self):
                    print(self.labelle,"'s McDonald’s farm has ",end="")
                    liste=self.get_animal_types()
                    print(liste)
       

    
        
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
macdonald.get_animal_types()
macdonald.Farmget_short_info()
