class A:
    def __init__(self):
        print("Constructor A")
class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor b")
class E(A):
      def __init__(self):
        super().__init__()
        print("Constructor e")      
class C(A):
    def __init__(self):
        super().__init__()
        print("Constructor c")
class D(B,C,E):
    def __init__(self):
        super().__init__()
        print("Constructor d")                        
obj=D()        