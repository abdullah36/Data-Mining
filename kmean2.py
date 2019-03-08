nd=int(input("Please enter no of data points\n"))
print("Please enter ",nd," data points")
dl=[]
for i in range(0,nd):
    temp=int(input())
    dl.append(temp)
while True:
    nc=int(input("Please enter no of clusters\n"))
    if(nc<nd):
        break
    
meanl=[0 for i in range(0,nc)]
for i in range(0,nc):
    meanl[i]=dl[i]

nestcc=[[] for i in range(0,nc)]
nestpc=[]
dif=[0 for i in range(0,nc)]
count=0

def largecc(nestcc):
    j=0
    l=[0 for i in range(0,nc)]
    for i in nestcc:
        l[j]=len(i)
        j=j+1
    return max(l)

def space(maxl,cclen):  
    l=["   " for i in range(0,maxl-cclen+2)]
    return " ".join(l)
    
    

while True:
    count=count+1
    nestpc.clear()     #clearing previous cluster list
    for i in nestcc:   #copying current in previous cluster and clearing current
        nestpc.append(list(i))
        i.clear()
        
    for i in dl:
        for j in meanl:
            dif[meanl.index(j)]=abs(i-j)
        index=dif.index(min(dif))
        nestcc[index].append(i)
    print()

    if(count==1):
       maxl=largecc(nestcc)
    
    print("Step ",count,"->")
    if(nestpc==nestcc):
            print("\nHence Final clusters are:")
    for i in range(1,nc+1):
        cclen=len(nestcc[i-1])
        print("cluster ",i,":",nestcc[i-1],end=space(maxl,cclen))
        print("Mean : ",meanl[i-1])
    for i in nestcc:
        meanl[nestcc.index(i)]=float(sum(i))/len(i)
    
    if nestpc==nestcc:
         break

  
        
        
