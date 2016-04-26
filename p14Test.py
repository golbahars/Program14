
        
set1 = CustomSet([1,3,1])
set2 = CustomSet([1,2,3,4,4])
result = set1>=set2
print("Is set1 a superset of set2?:",result)
result = set2>=set1
print("is set2 a superset of set1?:",result)

print("testing len...")
print("len of set1:",len(set1))

print("Testing print...")
print(set1)
