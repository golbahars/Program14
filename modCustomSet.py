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
