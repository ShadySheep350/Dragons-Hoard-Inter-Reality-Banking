from abc import ABC, abstractmethod
import math

class Coin(ABC):
    valueOfGold = 0

    @staticmethod #got slightly stuck here, so a hint of AI
    def convert(typeCoin, amount, toThisCoin):
        convertedAmount = math.floor(
            (amount * typeCoin.valueOfGold)
            / toThisCoin.valueOfGold
        )

        coinsUsed = round(
            (convertedAmount * toThisCoin.valueOfGold)
            / typeCoin.valueOfGold
        )

        return convertedAmount, coinsUsed
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

    def ConvertCoins(self): #Ai method
        coinTypes = {
            "copper": Copper,
            "silver": Silver,
            "electrum": Electrum,
            "gold": Gold,
            "platinum": Platinum
        }
        fromChoice = input("What coin are you converting from? ").strip().lower()
        toChoice = input("What coin are we converting to? ").strip().lower()
        typeCoin = coinTypes.get(fromChoice)
        toThisCoin = coinTypes.get(toChoice)

        if typeCoin is None or toThisCoin is None:
            print("That coin type was not recognized.")
            return

        amount = int(input(f"How many {typeCoin.__name__} coins are you converting? "))

        if amount > self.currencies[typeCoin]:
            print("You do not have that many coins.")
            return

        convertedAmount, coinsUsed = Coin.convert(
            typeCoin,
            amount,
            toThisCoin
        )

        if convertedAmount == 0:
            print(
                f"You do not have enough {typeCoin.__name__} "
                f"to create one {toThisCoin.__name__}."
            )
            return

        self.currencies[typeCoin] -= coinsUsed
        self.currencies[toThisCoin] += convertedAmount

        self.UpdateTotalValue()

        print(
            f"Converted {coinsUsed} {typeCoin.__name__} "
            f"into {convertedAmount} {toThisCoin.__name__}."
        )

        print(
            f"The remaining {typeCoin.__name__} coins were "
            f"returned to your account."
        )
        
        