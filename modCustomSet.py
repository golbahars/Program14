class CustomSet:
    def __init__(self,tmpList):
        for a in tmpList:
            while tmpList.count(a) > 1:
                tmpList.remove(a)
        self._setList = tmpList
    
    def __add__(self,other):
        for a in other:
            self._setList.append(a)
        newList = CustomSet.__init__(self._setList) 
        return newList
    
    def __and__(self,other):
        newList = self._setList
        for a in other:
            if a not in newList:
                newList.remove(a)
        return newList
        
                
