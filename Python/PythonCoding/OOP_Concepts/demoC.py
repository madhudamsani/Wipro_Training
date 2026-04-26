from OOP_Concepts.demoA import A
from  OOP_Concepts.demoB import B

class C(A, B):
    def __init__(self, n1, n2, msg):
        super().__init__(n1, n2)
        #super().__init__(msg)
        B.__init__(self, msg)

    def final(self):
        print('Done')
