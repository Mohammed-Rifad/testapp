class Bank:

    def __init__(self,name,age):
        self.uname = name
        self.age = age


    def display(self):
        print('hello',self.uname,self.age)

    @property
    def uname(self):
        print('getter working...')
        
        return self._uname  # if function name and instance variable are same, put underscore in instance variable
    
    @uname.setter
    def uname(self,new_name):
        print('setter working...')

        if(len(new_name) > 5):

            self._uname = new_name
        else:
            print('invalid name')
            
b= Bank('rifadhh',20)

print(b.uname)



