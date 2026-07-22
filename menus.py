import accounts
import sys


def HomeMenu(accountList):
    print("\n====Dragons Hoard Inter-reality Banking services====\n")
    
    while True:
        print("1: New Adventurer\n2: Party List\n3: Manage Party\n4: DM Stuff\n5: Exit")
        choice = int(input("Please make a selection: "))
        match choice:
            case 1:
                name = input("Welcome new member, please start by entering your name: ")
                account = accounts.Account(name)
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
                Party_List(accountList)

            case 3:
                pass
    
            case 4:
                pass

            case 5:
                print("Thanks for using Dragon's Hoard Banking! Thanks for your money.")
                sys.exit(0)

def AccountOptions(account):
    run = 1
    while run == 1:
        print("\n==== "+ account.name + "'s DashBoard===\n")
        choice = int(input("What would you like to do with your account?\n1: Add Coin\n2: Remove Coin\n3: Convert Coin\n4: Purchase History\n5: Menu\nChoice: "))

        match choice:
            case 1:
                pass

            

            case 5:
                run = 0

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
    print("No Matching Accounts, Please match your spelling in common. ")
    #create the menu based on selecting who is using, by calling their class and using the methods on selection