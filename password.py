n=int(input("ENTER 1 IF YOU WANT A PASSWORD"))
lst1=[0,1,2,3,4,5,6,7,8,9]
lst2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lst3=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lst4=['@','$','*','_','#']
i=1
j=1
k=1
l=1
for i in range(11):
    for j in range(27):
        for k in range(27):
            for l in range(5):
                print(str(str(lst1[i])+str(lst2[j])+str(lst3[k])+str(lst4[l])))
                l=l+1
                m=int(input("ENTER 1 IF YOU WANT A PASSWORD"))
                if(m==1):
                    continue
                else:
                    break
            k=k+1
        j=j+1
    i=i+1  
