my_dict={"bijender":45,"deepak":30,"parak":20,"anjili":30,"roshini":50}
new_dict={}
length=len(my_dict)
for i in range(length):
    max_1=0
    for value in my_dict:
        if max_1<my_dict[value]:
            max_1=my_dict[value]
            key=value
    new_dict.update({key:max_1})
    my_dict.pop(key)
print(new_dict)