class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def display(self):
       
        print( self._name ,  self.age )
    
    # Setting the person_name() function as a property using the @property decorator.
    @property
    def name(self) -> str:
        print('getter')
        return self._name

    
    @name.setter
    def name(self,new_name) ->None:
        print('setter')
        if(new_name != 'kji'):

            self._name = new_name
            print('if working')
    
        else:
            print('false')

Jack = Person("Jack", 26)
Jack._name = 'kji'

Jack.display()
# print("The name of the Person is:", Jack.name)