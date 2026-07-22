from abc import ABC, abstractmethod
import math

class Coin(ABC):
    valueOfGold = 0
    def convert(typeCoin,amount,toThisCoin):
            coinConvert = (amount * typeCoin.valueOfGold) // toThisCoin.valueOfGold #Check this after this varible is alive somewhere else 
            return coinConvert
        
    # will convert one amount of coin to the other coin. Will round down to the next coin
        #if going up to gold, coin.amount * valueOfgold
        #1 Copper (cp) = 0.01 gp1
        # Silver (sp) = 0.1 gp1 
        # Electrum (ep) = 0.5 gp1
        #  Gold (gp) = 1.0 gp1 
        # Platinum (pp) = 10.0 gp
class Copper(Coin):
    valueOfGold = .01
class Silver(Coin):
    valueOfGold = .1
class Electrum(Coin):
    valueOfGold = .5
class Gold(Coin):
    valueOfGold = 1
class Platinum(Coin):
    valueOfGold = 10


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
    def UpdateTotalValue(self):
        total = 0
        for typeCoin, amount in self.currencies.items():
            total += amount * typeCoin.valueOfGold
        self.totalValueGold = math.floor(total)

    def AddCoins(self):
        for typeCoin in self.currencies:
            amount = int(input(f"How many {typeCoin.__name__} coins will you deposit? "))
            self.currencies[typeCoin] += amount
            self.UpdateTotalValue()
        print(f"Crog, our coin counter has finished sorting through your bag and made the requested deposit.\n Your new total value stands at {self.totalValueGold}\n Your collection is now the following")
        for typeCoin in self.currencies:
            print(f"{typeCoin.__name__}: {self.currencies[typeCoin]}")

    def RemoveCoins(self,typeCoin,amount):
        for typeCoin in self.currencies:
            amount = int(input(f"How many {typeCoin.__name__} coins will you deposit? "))
            self.currencies[typeCoin] -= amount
            self.UpdateTotalValue()
        print(f"Crog, our coin counter has finished sorting through your bag and made the requested withdrawl.\n Your new total value stands at {self.totalValueGold}\n Your collection is now the following")
        for typeCoin in self.currencies:
                   print(f"{typeCoin.__name__}: {self.currencies[typeCoin]}") 
    def ConvertCoins(self,typeCoin,amount,ToThisCoin):
        ToThisCoin = input("What coin are we converting too? ")
        