#!/usr/local/bin/python3

class Dog:
    name=''
    breed=''
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

dogs=[]

while True:
     name=input('Name: ')
     if not name:
         break
     breed=input('Breed: ')
     cur_dog=Dog(name,breed)
     dogs.append(cur_dog)
     print('*'*40+'\nDogs')
     for key,dog in enumerate(dogs):
         print('%i. %s:%s'%(key,dog.name,dog.breed))
     print('*'*40)

