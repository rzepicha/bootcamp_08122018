class Vector:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __add__(self,drugi):
        return Vector(self.x+drugi.x,self.y+drugi.y)

    def __sub__(self, drugi):
        return Vector(self.x-drugi.x, self.y-drugi.y)

    def __mul__(self,drugi):
        if isinstance(drugi, Vector):
            return self.x*drugi.x+self.y*drugi.y
        if isinstance(drugi, int):
            return Vector(self.x * drugi, self.y * drugi)

    def length(self):
        return (self.x**2+self.y**2)**0.5

    def __lt__(self, drugi):
        return self.length()<drugi.length()



def test_vector_init():
    vector_1=Vector(x=1, y=2)
    assert vector_1.x==1
    assert vector_1.y==2

def test_vector_add():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1+vector_2
    assert vector_3.x==2
    assert vector_3.y==4
    assert vector_1.x==1
    assert vector_1.y==2


def test_vector_sub():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1-vector_2
    assert vector_3.x==0
    assert vector_3.y==0
    assert vector_1.x==1
    assert vector_1.y==2


def test_vector_mul():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1 *3
    assert vector_3.x==3
    assert vector_3.y==6
    assert vector_1.x==1
    assert vector_1.y==2


def test_vector_mul_vector():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    assert vector_1*vector_2==1*1+2*2
    assert vector_1.x==1
    assert vector_1.y==2

def test_vector_length():
    assert Vector(3,4).length()==5

def test_vector_lt():
    assert Vector(1,1)<Vector(1,2)
    assert (Vector(6,5)<Vector(5,5))==False

