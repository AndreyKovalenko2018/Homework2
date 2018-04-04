print('5)')
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
print(a,b,c)
if not a<b:
    a,b=b,a
if not a<c:
    c,a=a,c
if not b<c:
    c,b=b,c
print('a=',a)
print('b=',b)
print('c=',c)