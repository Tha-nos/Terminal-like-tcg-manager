from os import getcwd
from os import listdir
import time
def main():
    print("\nWelcome to MTG card manager,a terminal card manager emulator.")
    print("Loading card list...")
    time.sleep(1)
    if 'mylist.txt' in listdir(getcwd()):
        file=open("mylist.txt","r+")
        cards=[line.rstrip('\n') for line in file]
        print("\nList loaded")
    else:
        print("\nIt seems that the card list does not exist")
        print("Creating one now...")
        time.sleep(1)
        file=open("mylist.txt","w")
        cards=[]
        print("List created!")

    print("\nWhat do you want to do?")
    print("1.Create card list")
    print("2.Edit current card list")
    print("3.View current card list")
    print("4.Exit")
    answer=input(":")
    while True:
        if answer=="1":
            creation()
        elif answer=="2":
            edit()
        elif answer=="3":
            view()
        elif answer=="4":
            print("\nThanks for using MTG card manager!")
            file.close()
            break
        else:
            print("Please input a valid choice.")
        print("\nWhat do you want to do?")
        print("1.Create card list")
        print("2.Edit current card list")
        print("3.View current card list")
        print("4.Exit")
        answer=input(":")

def creation():
    print("\nCreating list...")
    cards=[]
    file=open("mylist.txt","w")
    answer=input("List created,do you want to add cards in it?Y/n:")
    if answer=='N' or answer=='n':
        print("Returning to main menu...\n")
        return
    elif answer=='Y' or answer=='y':
        finished=False
        print("Input card name,type 'exit' to exit.")
        while finished==False:
            card=input("Card:")
            if card!='exit':
                if card not in cards:
                    file.write("\n")
                    file.write(card)
                    cards.append(card)
            else:
                finished=True
                print("\nReturning to main menu...\n")
        return
    else:
        print("Not a valid input")
        print("Exiting...")
        return

def edit():
    print("Obtaining card list...")
    file=open("mylist.txt","r+")
    time.sleep(1) 
    print("List obtained")
    answer=input("Would you like to preview list before editing?Y/n:")
    if answer=='Y' or answer=='y':
        print(file.read())
    file=open("mylist.txt","r+")
    cards=[line.rstrip('\n') for line in file]
    answer=input("\nWould you like to add or remove cards?add/remove:")
    if answer=='add':
        print("Type 'exit' to stop editing")
        while True:
            card=input("Card:")
            if card!='exit':
                if card not in cards:
                    file.write("\n")
                    file.write(card)
                    cards.append(card)
            else:
                file.close()
                break
        print("Returning to main menu...")
        return
    elif answer=='remove':
        file=open("mylist.txt","r+")
        cards=[line.rstrip('\n') for line in file]#Card in line
        answer=input("Type cards to remove,type 'exit' to exit:")
        while answer!='exit':
            if answer in cards:
                cards.remove(answer)
            answer=input("Type cards to remove,type 'exit' to exit:")
        file=open("mylist.txt","w")
        finallist=[]
        for i in range(0,len(cards)):
            if cards[i]!="":
                finallist.append(cards[i])
        for i in range (0,len(finallist)):
            file.write("\n")
            file.write(finallist[i])
        print("Cards removed!")
        print("Returning to main menu...")
            
        
    
                    
            
        
        
        
        
    
        
        
        
        
