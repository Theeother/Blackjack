"""

Work By AKS 
Ahmed Khalil Seddik

"""
def para():
    decks=input("How many decks ?")
    minbet=input("Minimum bet = ?")
    DAS=input("Is 'double after split' offered ? (Y/N)")
    DAS=DAS.upper()=="Y"
    return(int(decks),minbet,DAS)

def count(cards,L):
    s=0
    for i in cards:
        if i=="2":
            s+=0.5;L[int(i)]-=1
        if i=="3":
            s+=1;L[int(i)]-=1
        if i=="4":
            s+=1;L[int(i)]-=1
        if i=="5":
            s+=1.5;L[int(i)]-=1
        if i=="6":
            s+=1;L[int(i)]-=1
        if i=="7":
            s+=0.5;L[int(i)]-=1
        if i=="8":
            s+=0;L[int(i)]-=1
        if i=="9":
            s-=0.5;L[int(i)]-=1
        if i=="0":
            s-=1;L[10]-=1
        if i=="1":
            s-=1;L[int(i)]-=1
    return(s)

def hardreset():
    decks,minibet,DAS=para()
    L = {i: 4*decks for i in range(1,10)}
    L[10]=16*decks
    return(decks,minibet,DAS,L,0,decks)

def HandD(cards,H,D):
    for i in range(len(cards)):
        if cards[i]==".":
            return("","")
        if cards[i]=="+":
            H+=cards[i+1]
        if cards[i]=="-":
            D=cards[i+1]
    return(H,D)

def HardSoft(H):
    H=list(H)
    if len(H)==2 and H[0]==H[1]!="0":return("Split")
    if "1" not in H:
        return("Hard")
    L=[]
    for item in H:
        L += [10] if item == "0" else [int(item)]
    L+=[10]
    return(["Soft","Hard"][sum(L)>21])

def Hard(H,D):
    D = [int(D),int(D)+10][D in ["0", "1"]]
    H=list(H)
    H=[int(x) if x!="0" else 10 for x in H]
    total=sum(H)
    print("Hard",total,"V",D)
    if total<=8:print("Hit")
    if total>=17:print("Stand")
    if 13<=total<=16:
        if 2<=D<=6:print("Stand")
        else:print("Hit")
    if total == 10:
        if D<=9:print("Double if allowed atherwise Hit")
        else:print("Hit")
    elif total == 11:
        if D==1:print('Hit')
        else:print("Double if allowed atherwise Hit")
    elif total == 12:
        if 4<=D<=6:print("Stand")
        else:print("Hit")
    elif total == 9:
        if 3<=D<=6:print("Double if allowed atherwise Hit")
        else:print("Hit")
        
def Soft(H,D):
    D = [int(D),int(D)+10][D in ["0", "1"]]
    H=list(H)
    H=[int(x) if x!="0" else 10 for x in H]
    total=sum(H)-1
    print("Soft",total+11,"V",D)
    if total>=8:print("Stand")
    if (
        total in [5, 4]
        and 4 <= D <= 6
        or total not in [5, 4]
        and total == 6
        and 3 <= D <= 6
    ):
        if 4<=D<=6 :print("Double if allowed atherwise Hit")
    elif total in [5, 4, 6]:
        print("Hit")
    elif total == 7:
        if D<=6:print("Double if allowed atherwise Stand")
        if 7<=D<=8:print("Stand")
        else:print("Hit")
    if total<=3:
        if 5<=D<=6:
            print("Double if allowed atherwise Hit")
        else:
            print("Hit")

def Split(H,D,DAS):
    D = [int(D),int(D)+10][D in ["0", "1"]]
    H=int(H)
    if H in {0, 5}:
        Hard(str(H)*2,D)
    elif H in {1, 8}:
        print("Split")
    elif H == 4:
        if D in [5, 6] and DAS:print("Split")
        else:Hard(str(H)*2,D)
    elif H == 6:
        if D == 2 and DAS or D != 2 and 2 < D < 7:print("Split")
        else:Hard(str(H)*2,D)
    elif H == 7:
        if D<8:print("Split")
        else:Hard(str(H)*2,D)
    elif H == 9:
        if D in [7,10,11]:Hard(str(H)*2,D)
        else:print("Split")
    if H in {3, 2}:
        if D < 4 and DAS or D >= 4 and D < 8:
            if DAS:print("Split")
        else:
            Hard(str(H)*2,D)






        
decks,minibet,DAS,L,score,IDC=hardreset()
H,D="",""

#game starts
print("type 'help' for help")
while 1:
    print('???')
    ese=input()
    if ese=="gogogo":
        while 1:
            cards=input("cards delt are:")
            if cards=="exit":break
            decks=sum(L.values())/52
            print("           ")
            score+=count(cards,L)
            TC=score/decks
            H,D=HandD(cards,H,D)
            print("Running count=",score)
            print(" "*10,"cards delt/left=",IDC*52-sum(L.values()),"/",sum(L.values()))
            print(" "*15,"Deck penetration= ",round((IDC*52-sum(L.values()))/(IDC*52)*100,2),"%")
            print("True count=",round(TC,2))
            if HardSoft(H)=="Hard" and D!="" and len(H)>=2:
                Hard(H,D)
            if HardSoft(H)=="Soft" and D!="" and len(H)>=2:
                Soft(H,D)
            if HardSoft(H)=="Split" and D!="" and len(H)>=2:
                H=H[0]
                Split(H,D,DAS)
            
            
            if cards=="r":decks,minibet,DAS,L,score,IDC=hardreset();H,D="",""
            
    if ese=="help":
        print("type 'gogogo' to start")
        print("input cards delt, with 10s=0, no space needed")
        print("your cards should be preceeded with a '+' ")
        print("dealer's card should be preceeded with a '-'")
        print("at the end of the hand input '.' to reset hands")
        print("to reset the decks press 'r'")
        print("to exit the counter input 'exit'")
        print("Made by AKS")
        print("https://www.instagram.com/theotheraks/")
        print("https://www.reddit.com/user/TheOtherAKS")
