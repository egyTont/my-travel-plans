class Parent():
    def __init__(self,last_name,eye_color):
        print("parent thing called") 
        self.last_name=last_name
        self.eye_color=eye_color
class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print"child thing started"
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys=number_of_toys
#jimy_again = Parent("cyrus","blue")
#print(jimy_again.last_name)

brad=Child("cyrus","blue",5)
print(brad.last_name)
print(brad.number_of_toys) 

        
