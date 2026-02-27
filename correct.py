counter = 0
for i in range(2,10):
    for j in range(2,i-1):
        if(j != 1):
            if(i % j == 0):
                counter += 1
    if(counter == 0):
        print(f'{i} is Aval')
    counter = 0
    
print('Good job, you found Avl number in range (0,10)')
print('Ok')
                
    
    