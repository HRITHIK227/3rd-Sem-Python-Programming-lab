list1=[10,10.5,'Apple',34,47]
length=len(list1)
while(1):
    print('*****List Iteration*******')
    print('1.Using For loop')
    print('2.Using for with range')
    print('3.Using while')
    print('4.Using List Comprehension')
    print('5.Using Enumeration')
    print('6.Exit')
    m=int(input('Enter your choice'))
    if(m==1):
        for i in list1:
            print(i)
    elif(m==2):
        for i in range(length):
            print(list1[i])
    elif(m==3):
        i=0
        while i < length:
            print(list1[i])
            i += 1
    elif(m==4):
        [print(i) for i in list1]
    elif(m==5):
        for i, val in enumerate(list1):
            print (i, ",",val)
    else:
        print('Exit from the program')
        break




