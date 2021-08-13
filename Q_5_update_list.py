list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,] 
i=0
dic1={}
length=len(list1)
while i<length:
    my_dic={list1[i]:list2[i]}
    dic1.update(my_dic)
    i=i+1
print(dic1)



# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,] 
# i=0
# dic={}
# length=len(list1)
# while i<length

