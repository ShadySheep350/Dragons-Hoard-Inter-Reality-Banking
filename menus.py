import accounts
import sys


def HomeMenu(accountList):
    print("\n====Dragons Hoard Inter-reality Banking services====\n")
    
    while True:
        print("1: New Adventurer\n2: Party List\n3: Manage Party\n4: DungeonMaster's Tools\n5: Flee") 
        choice = int(input("Please make a selection: "))
        match choice:
            case 1:
                name = input("Welcome new member, please start by entering your name: ")
                account = accounts.Account(name)
                accountList.append(account)
                print(account.name +", Welcome to the Party. We hope you have coin!")
                for typeCoin in account.currencies:
                    amount = int(input(f"How many {typeCoin.__name__} coins do you have? "))
                    account.currencies[typeCoin] = amount
                account.UpdateTotalValue()
                print(f"You have {account.totalValueGold} total in gold")
                if account.totalValueGold >= 3000:
                    print("Exellent you're a good one.")
                elif account.totalValueGold >= 1000:
                    print("Eh, you're alright...")
                else:
                    print("Yikes, you're no good to us. Whatever. *oh right* Ahem WELCOME!")

            case 2:
                Party_List(accountList)

            case 3:
                pass
    
            case 4:
                pass

            case 5:
                print("Thanks for using Dragon's Hoard Banking! Its saver with us then you.")
                sys.exit(0)

def AccountOptions(account):
    run = 1
    while run == 1:
        print("\n==== "+ account.name + "'s DashBoard===\n")
        print(f"===Your Worth: {account.totalValueGold}")
        choice = int(input("What would you like to do with your account?\n1: Save Coin\n2: Spend Coin\n3: Convert Coin\n4: Purchase History\n5: Return to Menu\nChoice: "))
        print("")

        match choice:
            case 1:
                account.AddCoins()
                 

            

            case 5:
                run = 0

def DmMenuOptions():
    pass

def Party_List(accountList):
    print("\n==== Party Accounts ====\n")

    if len(accountList) == 0:
        print("No adventurers have opened accounts.\n")
        return

    for account in accountList:
        print(account.name)
    choice = input("\nWho is using our service? ")
    for account in accountList:
        if account.name.lower() == choice.lower():
            AccountOptions(account)
            return
    print("No Matching Accounts, Please ensure you're spelling in common. ")
    #create the menu based on selecting who is using, by calling their class and using the methods on selection