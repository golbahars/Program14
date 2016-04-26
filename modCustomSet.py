class CustomSet:
    def __init__:(self, tmpList):
        self._setList = [a for a in tmpList if a not in self._setList]
    def __gt__(self, tmpSet):
        """Description: checks if tmpSet is a superset of self
        PreCond: self(list),tmpSet(list)
        PostCond: returns true if it is a superset. returns false if not.
        """
        numct = 0
        for ct in range(0,len(self)):
            if self[ct] in tmpSet:
                numct +=1
        if ct == len(self):
            return True
        else:
            return False
    def __len__(self):
        """Description: counts elements in list
        PreCond:self(list)
        PostCond:returns count
        """
        tmpCT=0
        alreadyCT = []
        for ct in range(0,len(self)):
            if self[ct] not in alreadyCT:
                tmpCT +=1
                alreadyCT.append(self)
        return tmpCT
    def __str__(self):
        """Description: prints list
        PreCond:self(list)
        PostCond:returns string
        """
        tmp = "{ "
        for ct in range(0,len(self)-1):
            tmp+=str(self[ct])+", "
        tmp+=str(self[-1]) +" }"
        return tmp
