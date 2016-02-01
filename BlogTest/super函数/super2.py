class Base():
    def __init__(self):
        print('Base')

class A(Base):
    def __init__(self):
        print('A')
        Base.__init__(self)

class B(Base):
    def __init__(self):
        print('B')
        Base.__init__(self)

class C(A, B):
    def __init__(self):
        print('C')
        A.__init__(self)
        B.__init__(self)

c= C()
