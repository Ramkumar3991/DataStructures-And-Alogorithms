def swapAsc(list1):
    for j in range(0,int(le)):
        for i in range(0,int(le)-1):
            if list1[i] > list1[i+1]:
                temp=list1[i]
                list1[i]=list1[i+1]
                list1[i+1]=temp
    print("The Ascending order "+str(list1))

def swapDsc(list1):
    for j in range(0,int(le)):
        for i in range(0,int(le)-1):
            if list1[i] < list1[i+1]:
                temp=list1[i]
                list1[i]=list1[i+1]
                list1[i+1]=temp
    print("The Descending order "+str(list1))   
        
        
list1 = []
le=input("Enter the length ")
for k in range(0,int(le)):
    element=input("Enter the " + str(k+1) + " Element ")
    list1.append(int(element))
    
swapAsc(list1)
swapDsc(list1)
  