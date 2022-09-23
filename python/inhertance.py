#Create three methods in each class, 2 methods are specific to each class and third method (override method) should be in all three Classes A, B and C

class A:
    def __init__(self, name, email):
        self.name = name
        self.email = email 

    class B:
        def __init__(self, fname, lname):
            self.name = fname
            self.email = lname   
    class C:
        def __init__(self, age, height):
            self.name = age
            self.email = height         



class D:
    pass