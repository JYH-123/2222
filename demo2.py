冒泡排序

list =[231,21413,52,242,52,432,234]
for i in range(len(list)):
    for j in range(len(list)-i-1):
        if list[j] >list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            
print(list)