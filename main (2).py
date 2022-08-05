def func(list1):
    repeat = []
    _size=len(list1)
    for i  in range(_size):
  
        k=i+1
  
        for j in range(k,_size):
            if list1[j]==list1[i] and list1[j] not in repeat:
                repeat.append(list1[j])
     
    return repeat
 
list1= [1,2,3,1,"abc","ab","bc","abc"]
print(func(list1))
    
