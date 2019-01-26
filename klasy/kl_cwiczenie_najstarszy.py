class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age



def najstarszy(*args):
    lista=[]
    for dog in args:
        lista.append([dog.age, dog])

    lista.sort()
    return lista[-1][1]



kot = Dog("Kot", 1)
pies = Dog("Pies", 8)
rex = Dog("rex", 19)

x=najstarszy(kot,pies,rex)
print(x.name)