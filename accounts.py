from abc import ABC, abstractmethod

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
    def AddCoins(self,typeCoin,amount):
        pass
    def RemoveCoins(self,typeCoin,amount):
        pass
    def ConvertCoins(self,typeCoin,amount,ToThisCoin):
        pass