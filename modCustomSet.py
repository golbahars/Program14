class CustomSet:
    def __init__(self,tmpList):
        for a in tmpList:
            while tmpList.count(a) > 1:
                tmpList.remove(a)
        self._setList = tmpList
        
    def __add__(self,other):
        newList = [a for a in self._setList]
        for a in other._setList:
            newList.append(a)
        newList = CustomSet(newList)
        return newList
    
    def __and__(self,other):
        newList = [a for a in self._setList if a in other._setList]
        return newList
