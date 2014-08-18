import sys
import unittest
from datagen import *
from random import choice, randint, shuffle

class exp_01:
    def __init__(self,a,b,result):
        self.a = a
        self.b = b
        self.result = result

    def add(self):
        temp = self.a + self.b
        self.result += temp
        print(self.result)

    
class obj_test(Object):
    def __init__(self, world, dep, spec, prof):
        
        self = Object("course")
        
        
        self.department = dep
        self.specialization = spec
        self.prof = prof     
        self["difficulty"] = AttrDist({"easy": 0.7, "hard": 0.3}).generate()
        
        world.addObject(self)

world = World()

instant = exp_01(5,6,0)
array = [[5,0,0,5],[5,0,0,0]]

obj = obj_test(world,'EE','test','RCL')

#exp_01.add(instant)

#print(array[1][1])
#print(len(array[1]))

#print(array[i][j] for i in len(array) for j in len(array[i]))



#print[rel for i in array for rel in i]
#print[rel for rel in array]
