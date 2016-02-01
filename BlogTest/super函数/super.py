class Base():
    def __init__(self):
        print('Base')

class A(Base):
    def __init__(self):
        print('A')
        mro = self.__class__.__mro__
        mro[mro.index(A)+1].__init__(self)
        #super(A, self).__init__()

class B(Base):
    def __init__(self):
        print('B')
        mro = self.__class__.__mro__
        mro[mro.index(B)+1].__init__(self)
        #super(B, self).__init__()

class C(A, B):
    def __init__(self):
        print('C')
        #super(C, self).__init__()
        mro = self.__class__.__mro__
        mro[mro.index(C)+1].__init__(self)
        

c= C()
