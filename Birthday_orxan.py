c=0
print('set1:1,3,5,7,9,11,13,15,17,19,21,2325,27,29,31')
answer=input('y for yes n for no')
if answer=='y':
    c+=1
print('set2:2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31')
answer=input('y for yes n for no')
if answer=='y':
    c+=2
print('set3:4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31')
answer=input('y for yes n for no')
if answer=='y':
    c+=4
print('set4:8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31')
answer=input('y for yes n for no')
if answer=='y':
    c+=8
print('set5:16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31')
answer=input('y for yes n for no')
if answer=='y':
    c+=16
print(c)