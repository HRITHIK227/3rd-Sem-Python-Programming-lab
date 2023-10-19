mylist=[1,3,6,8,10,13,15]
def linearsearch(mylist,x):
    for i in range(len(mylist)):
        if mylist[i]==x:
            return i
    return -1

def binarysearch(mylist,l,r,x):

    while l<=r:
        mid=int(l+r)//2
        #print("mid:",mid)
        if mylist[mid]==x:
            return mid
        elif mylist[mid]<x:
            l=mid+1
        else:
            r=mid-1
    return -1

print(mylist)
while(1):
    print('1.Linear Search')
    print('2.Binary Search')
    print('3.Exit')
    c= int(input('Enter your Choice'))
    if(c==1):
        x=int(input())
        print(mylist)
        ans=linearsearch(mylist,x)
        if(ans==-1):
            print('Element is not found')
        else:
            print('Element position is',ans)
    elif(c==2):
        x=int(input())
        print(mylist)
        l=0
        r=len(mylist)-1
        ans=binarysearch(mylist,l,r,x)
        if(ans==-1):
            print('Element is not found')
        else:
            print('Element position is',ans)
    elif(c==3):
        print('Exit from the program')
        break


