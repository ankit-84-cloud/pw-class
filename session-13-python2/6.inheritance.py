class parent:
    def testparent(_):
        print("Hello from parent ")

class child(parent):
    def testchild(_):
        print("Hello from child ") 

c = child("ankit") #pass value to constructor of parent class
c.testchild()
c.testparent()#child class can access parent class methods