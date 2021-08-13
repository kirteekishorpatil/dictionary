my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
i=0
a=[]
max=my_dict
while i<len(my_dict):
    if my_dict>max:
        max= my_dict
        a.append(max)
print(a)

    
    