A=[1,2,3,4,5,6,7,8,9]
C=['|| {:2}' , ': {:2}',': {:2}']
#print(A[2:6])
#print(A.pop(2:5))

a='|| {:2} :'
b=' {:2} :'
c=a+b
B=[1,2]
# print(c.format(*B))
C= ''.join(C)
print(C)
limit=["="]*len(C)
limit=''.join(limit)
#print(limit)

#print(((36**0.5)%1)==0)

d= '1,2,3,4'
#print(d.isnumeric())
e=list(d)
#print(e)
f='1234'
g=list(f)
h=str(g)

print(h,h.isnumeric())
for i in range(len(h)):
    print(h[i])