''' golbahar's methods'''

def __sub___(self,other):
    '''retuens a new set with elements in first set but not the second
       precondition: other is a type CustomeSet
       postcondition: None
    '''
       

    return self._setList - other._setList

def membership(self,element):
     '''checks if the element is a member of the set
       precondition: element is a type int
       postcondition: a type Bool is returned
    '''
    if element in self._setList:
        return True
    else:
        return False

def __ge__(self,other):
    '''checks if a set is the subset of another set
       precondition: other is a type CustomeSet
       postcondition: a type Bool is returned
    '''
    return self._setList >= other._setList
