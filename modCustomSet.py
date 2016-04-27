class CustomSet:
    def __init__(self,tmpList):
        for a in tmpList:
            while tmpList.count(a) > 1:
                tmpList.remove(a)
        self._setList = tmpList
        
    def __add__(self,other):
        newList = [a for a in self._setList]
        newList+= [a for a in other._setList]
        newList = CustomSet(newList)
        return newList
    
    def __and__(self,other):
        newList = [a for a in self._setList if a in other._setList]
        newList = CustomSet(newList)
        return newList
