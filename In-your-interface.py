#Ron Osborne SWDV 630 2W22/SP2
#In your interface assignment
#3/13/2022

class Teams:
    def __init__(self, members):
        self.__myTeam = members
        self.__index = -1
        
    def __len__(self):
        return len(self.__myTeam)

#Adding the __contains__ function here. Testing to see if a value passed in is contained in the iterable.
    
    def __contains__(self, val):
        if val in self.__myTeam:
            return True
        else:
            return False

#Adding the __iter__function here. This makes sure that the objects can be iterated.
    def __iter__(self):
        return self

#Addin the __next__ function. When called, this will iterate through the objects using an index and will print the object value for each index value.
#Once the end of the iterable is reached, it stops the iteration using StopIteration
    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.__myTeam):
            self.__index = -1
            raise StopIteration
        else:
            return self.__myTeam[self.__index]

#This function checks to see if the __len__ function is able to be called and if not prints an error message to the screen indicating as such.
    def __haslen__(self):
        try:
            print(len(self))
        except TypeError:
            print('No len method supported in this class')
    
def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print ('The number of classmates is', len(classmates))
    
    #Check to see if Tim and Sam are in the classmates object list.
    print('Are Tim and Sam both contained in the list of classmates?', 'Tim' and 'Sam' in classmates)
    
    #Demonstrates the __iter__ function being called on classmates.
    iter1 = classmates.__iter__()
    #Calling the __next__ function and printing the next value through the iteration.
    print (iter1.__next__())

    #Just printing each member of classmates.
    for t in classmates:
        print (t)
    
    #Checking to see if the __haslen__ function can be called (len).
    print('The number of classmates is: ',end="")
    classmates.__haslen__()
    #print(check)
    
    
main()
