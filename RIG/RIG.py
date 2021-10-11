#Inspiration Machine
from random import randint as num

class RIG:

    def object_writer(RIG,writen):
        with open("Inspo.txt","a") as file:
            file.write(f"{writen}\n")

    def object_chooser(RIG,list,length):
        with open(f'{list}.txt') as file:
            counter = 0
            line = num(1,length)
            for data in file:
                counter += 1
                objects = data.strip().split("\n")
                if line == counter:
                    return(objects[0])
    def inspo_combo(RIG):
        object = RIG.object_chooser("objects",231)
        theme = RIG.object_chooser("themes",357)
        emotion = RIG.object_chooser("emotions",232)
        question = RIG.object_chooser("questions",30)
        RIG.object_writer(f"{object} {theme} {emotion} {question}")
        return(object,theme,emotion,question)

