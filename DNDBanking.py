import _json
from abc import ABC, abstractmethod
import sys

def main():
    accountList = []
    homemenu(accountList)
    
    #  features:
    #  saved data
    #  gold converter
    #  formatted recipt .txt file writer
    # sort or search purchases
    # accounts for DM's with party gold total/spending logged, DM Loans ( under account options, d20 table on what intrest (one chicken leg, or 5X the loan back) is, as it is run by goblins)
    # logs Deposits and withdrawls on DM side, and updates party gold supply

    #How would I set up a list for accounts to display with this current structure that can later save to a Json
def homemenu(accountList):
    print("\n====Dragons Hoard Inter-reality Banking services====\n")
    
    while True:
        print("1: New Adventurer\n2: Party List\n3: Manage Party\n4: DM Stuff\n5: Exit")
        choice = int(input("Please make a selection: "))
        match choice:
            case 1:
                name = input("Welcome new member, please start by entering your name: ")
                accountList = []
                account = Account(name)
                accountList.append(account)
                print(account.name +", Welcome to the Party. We hope you have coin!")
                account.totalValueGold = int(input("How much gold are you giving us? Uh... How much is your worth in gold?\n"))
                if account.totalValueGold >= 3000:
                    print("Exellent you're a good one.")
                elif account.totalValueGold < 3000 and account.totalValueGold >= 1000:
                    print("Eh, you're alright I guess, nothing special...")
                elif account.totalValueGold < 1000:
                    print("Yikes, you're no good to us. Whatever. *oh right* Ahem WELCOME!")

            case 2:
                party_list(accountList)

            case 3:
                pass
    
            case 4:
                pass

            case 5:
                print("Thanks for using Dragon's Hoard Banking! Thanks for your money.")
                sys.exit(0)

def accountOptions(account):
    run = 1
    while run == 1:
        print("\n===="+account.name+"'s DashBoard===\n")
        choice = int(input("What would you like to do with your account?\n1: Add Coin\n2: Remove Coin\n3: Convert Coin\n4: Purchase History\n5: Menu\nChoice: "))

        match choice:
            case 1:
                pass

            

            case 5:
                run = 0

def party_list(accountList):
    print("\n==== Party Accounts ====\n")

    if len(accountList) == 0:
        print("No adventurers have opened accounts.\n")
        return

    for account in accountList:
        print(account.name)
    choice = input("Who is using our service? ")
    print("\n")
    for account in accountList:
        if account.name.lower() == choice.lower():
            accountOptions(account)
        else: print("No Matching Accounts")
    #create the menu based on selecting who is using, by calling their class and using the methods on selection


class Account():
    def __init__(self, name):
        self.name = name
        self.totalValueGold = ""
        self.currencies = {
            Copper: 0,
            Silver: 0,
            Electrum: 0,
            Gold: 0,
            Platinum: 0,   
        }

   

class coin(ABC):
    valueOfGold = ""
    def convert(Coin,amount,tothisCoin):
        # coinConvert = (amount * Coin.valueOfGold) // tothisCoin.valueOfGold #Check this after this varible is alive somewhere else 
        # return coinConvert
        pass
    # will convert one amount of coin to the other coin. Will round down to the next coin
        #if going up to gold, coin.amount * valueOfgold
        #1 Copper (cp) = 0.01 gp1
        # Silver (sp) = 0.1 gp1 
        # Electrum (ep) = 0.5 gp1
        #  Gold (gp) = 1.0 gp1 
        # Platinum (pp) = 10.0 gp
class Copper(coin):
    valueOfGold = .01
class Silver(coin):
    valueOfGold = .1
class Electrum(coin):
    valueOfGold = .5
class Gold(coin):
    valueOfGold = 1
class Platinum(coin):
    valueOfGold = 10

        
    


    
         


    

if __name__=="__main__":
        main()