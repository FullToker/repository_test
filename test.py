from copy import deepcopy
import copy

'''
list1=[1,2,[3,4]]
list2=deepcopy(list1)
list3= list1.copy()
list2[0]=5
list2[2][0]=6
list3[0]=5
list3[2][0]=6
print(list1,list2,list3)

list1= [(1,2),(3,4)]
list2= copy.deepcopy(list1)
list2[0]=[1,2]
print(list1,list2)
print(id(list1))
print(id(list2))
'''

def f(n):
    return n*2 if n<10 else n/2

print(f(f(9)),f(f(12)))
print("tz""")
print("桃子"*3)

print(all([]),all([[]]))

number=8
def test():
    print(number)

test()