import dice
print("🧗‍♂️"*10,"HiILL CLIMB FALL","🧗‍♂️"*10)
player1=input("enter player1 name : ")
player2=input("enter player2 name : ")
list_a=[]
list_b=[]
i=0
while(sum(list_a)!=10 and sum(list_b)!=10):
    if(i%2==0 and input("player1 enter p to  play: ")=='p'):
        if(sum(list_a)<10):
            diceno=dice.diceroll()
            print("\nDice no.-->",diceno)
            list_a.append(diceno)
        else:
            list_a.clear()
        print("step No.-->,",sum(list_a))
        i+=1
    elif(i%2!=0 and input("player2 enter p to  play: ")=='p'):
        if(sum(list_b)<10):
            diceno=dice.diceroll()
            print("\nDice no.-->",diceno)
            list_b.append(diceno)
        else:
            list_b.clear()
        print("step No.-->,",sum(list_a))
        i+=1
    else:
        break
if(sum(list_a)==10):
    print(player1,"is the winner..🥳")
elif(sum(list_b)==10):
    print(player2,"is the winner..🥳")
else:
    print("thankyouu!!!")        