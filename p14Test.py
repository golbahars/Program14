class CustomSet:
    def __init__(self,tmpList):
        for a in tmpList:
            while tmpList.count(a) > 1:
                tmpList.remove(a)
        self._setList = tmpList
        
