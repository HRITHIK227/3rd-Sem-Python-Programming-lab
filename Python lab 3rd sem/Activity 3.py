str="Welcome to Python World"
print('Original string:',str)
while(1):
    print('1.Count no of alphabets')
    print('2.Extract Character using range')
    print('3.String is alphnumeric or not')
    print('4.Exit')
    c=int(input('Enter your choice'))
    if(c==1):
        l=len([ele for ele in str if ele.isalpha()])
        print(l)
    elif(c==2):
        start=int(input('Enter start range'))
        end=int(input('Enter end range'))
        print(str[start:end])
    elif(c==3):
        print(str)
        b=str.isalnum()
        print(b)
    elif(c==4):
        break;
    


