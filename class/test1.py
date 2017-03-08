class Batva:
    def __init__(self, name, x):
        self.name=name
        self.x=x

    def show(self):
        print('Class Batva')

class Sheluha(Batva):
    def show(self):
        print('Class Sheluha')

class New_B(Batva):
    pass

f=Batva('Kate', 28)
g3=New_B('Alex',31)

g3.show()