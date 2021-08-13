c={}
i=1
while i<=15:
    a=(i,i**2)
    i=i+1
    c.update({a})
print(c)