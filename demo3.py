选择排序


list =[231,21413,52,242,52,432,234]
for i in range(len(list)-1):
    for j in range(len(list)-i-1):
        if list[i]>list[j+i+1]:
            list[i],list[j+i+1]=list[j+i+1],list[i]
            
 print(list)
        
