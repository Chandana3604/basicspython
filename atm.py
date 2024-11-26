print("*"*20,"ATM Machine","*"*20)
amount=int(input("enter the amount :"))
l=[500,200,100,50,20,10,5,2,1]
count=0
res=0
for i in l:
    notes=amount//i
    print(i,"notes",notes)
    count=count+notes
    amount=amount%i
   
    if count==1:
       res=res+count  
print("single notes:",count)