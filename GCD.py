x = 12
y = 30
a=[]
b=[]
c=[]
for i in range(1,x+1):
  if x%i==0:
    a.append(i)
for j in range(1,y+1):
  if y%j==0:
    b.append(j)
for elem in a:
  if elem in b:
    c.append(elem)
sorts =len(c)
print(c[sorts-1])
print("")

