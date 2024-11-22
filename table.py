print("***********Multiplication Table***********")
while True:
    x=int(input("enter your number : "))
    if(x==0):
        print("Thank youu!!")
        break
    else:
        for i in range(0,11):
            print(x,"*",i,"=",x*i)