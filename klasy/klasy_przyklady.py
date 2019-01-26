class Animals:
    pass

python = Animals()
python.imie="Rex"
python.wiek=10
python.grupa="Gady"




class Animal:
    def __init__(self, name, age, species):
        self.name=name
        self.age=age
        self.species=species
        self.energy=1100

    def nakarm(self):
        self.energy+=10

rex=Animal("Rex", 10, "canis familiaris")
print(rex.name)
print(rex.age)

rex.energy=rex.energy+10
print(rex.energy)
rex.nakarm()
print(rex.energy)

Animal.nakarm(rex)
print(rex.energy)

