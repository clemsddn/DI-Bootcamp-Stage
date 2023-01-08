from xp import Dog
from random import choice,shuffle
class PetDog(Dog):
    def __init__(self, name, age, weight,trained = False):
        super().__init__(name, age, weight)
        self.trained=trained
    def train(self):
        print(f'\n{self.bark()}')
        self.trained=True
    
    def play(self,*args):
        for dog in range(len(args)-1):
            print(dog,',',end="")
        print('and',args[-1],',',end="")
        print(' all play together')
    
    def do_a_trick(self):
        actions=['dog_name does a barrel roll','stands on his back legs','shakes your hand','plays dead']
        if self.trained :
            shuffle(actions)
            print(f'\n{self.name} {choice(actions)}.')

dog=PetDog('Bobly',10,50,True)
dog.do_a_trick()
dog.play('dg1','dg1','dg1','dg1')