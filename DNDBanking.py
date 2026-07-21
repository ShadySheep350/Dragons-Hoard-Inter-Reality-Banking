import _json
from abc import ABC, abstractmethod

def main():
    pass
    #  features:
    #  saved data
    #  gold converter
    #  formatted recipt .txt file writer
    # sort or search purchases
    # accounts for DM's with party gold total/spending logged, DM Loans ( under account options, d20 table on what intrest (one chicken leg, or 5X the loan back) is, as it is run by goblins)
    # logs Deposits and withdrawls on DM side, and updates party gold supply
    #
def homemenu():
    print("====Dragons Hoard Inter-reality Banking services====\n")
    print("1: New Adventurer\n 2: Existing Accounts\n3: Manage Party\n4:")
    choice = input("Please make a selection: ")
def accountOptions():
    print("What would you like to do with your account?")

class account():
    def __init__(self, name):
        self.name = ""
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
    #will convert one amount of coin to the other coin. Will round down to the next coin
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