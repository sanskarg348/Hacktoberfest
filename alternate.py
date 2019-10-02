n=int(input("Please enter the number of elements you want to enter: "))
mylis=[]
i=0
for i in range (0,n):
    elem=int(input("Enter the element: "))
    mylis.append(elem)
for i in range(0,n):
    if(i%2==0):
        print(mylis[i])
        
