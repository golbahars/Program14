''' testing golbahar's methods'''
__author__ = 'Golbahar Sadatrezaei'
__date__='26 April 2016'

s1= CustomSet([1,2,3,4])
s2= CustomSet([4,2,5,6])
print('testing the difference method')
print(s1-s2)
print('teting the membership method')
print(s1.membership(2))
print(s1.membership(0))
print('testing subset method')
print(s1<=s2)
print(s2<=s1)
