class Student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
    def display(self):
        print (f"Name: {self.name} ID: {self.id}" f" Marks: {self.marks}")
    def delete(self):
        result= self.marks>=40
        if result:
            print("passed")
        else:
            print("failed")

styl1=Student("18","John",85)  #object creation
styl1.display()
styl1.delete()