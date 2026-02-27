i = 1
m = 0
while i < 12:
    for n in range(1,i):
         while m < 12 - i:
            print(' ',end='')
            m += 1
         print(n,end=' ')
    m = 0
    print('')
    i += 1
    print('Good job')
    Alist =  [i for i in range(20) if i % 2 == 0]
        