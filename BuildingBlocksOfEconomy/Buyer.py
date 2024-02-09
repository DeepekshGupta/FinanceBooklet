class Buyer:



    def __init__(self, name, Total_Money, Total_Credit):
        self.name = name
        self.Total_Money = Total_Money
        self.Total_Credit = Total_Credit
        self.Total_Value = Total_Money + Total_Credit
        self.Total_Spending = 0
        self.Total_Assets = {}

    def getName(self, name):
        return self.name
    def getTotalMoney(self):
        return self.Total_Money
    def getTotalCredit(self):
        return self.Total_Credit
    def getTotalValue(self):
        return self.Total_Value
    def getTotalSpending(self):
        return self.Total_Spending
    def getAssets(self):
       return self.Total_Assets
       
    

# ---------------------------------------------------------------------
    def giveMoney(self, amt):
        self.Total_Money -= amt
        self.updateAccounts(amt, 0)       
        print("transaction completed: transfered " + str(amt) + " Money to seller")
        return amt
    
    def takeMoney(self, amt):
        self.Total_Money += amt
        self.updateTotalValueAdd(amt)       
        print("transaction completed: recieved " + str(amt) + " Money from buyer")
        return amt
   
    def giveCredit(self, amt):
        self.Total_Credit -= amt
        self.updateAccounts(0, amt)       
        print("transaction completed: transfered " + str(amt) + " Credit to seller")
        return amt 

    def takeCredit(self, amt):
        self.Total_Credit += amt
        self.updateTotalValueAdd(amt)       
        print("transaction completed: recieved " + str(amt) + " Credit from buyer")
        return amt
   

    def updateTotalValueAdd(self, amt):
        self.Total_Value += amt
        return self.Total_Value
    
    # def updateTotalSpendingAdd(self, money, credit):
    #     totalSpending = (money + credit)
    #     self.Total_Spending += totalSpending
    #     return totalSpending
   
    # def updateAccountsAdd(self, money, credit):
    #     self.updateTotalValue(self.updateTotalSpending(money, credit))

    def updateTotalValue(self, totalSpending):
        self.Total_Value -= totalSpending
        return self.Total_Value
    
    def updateTotalSpending(self, money, credit):
        totalSpending = (money + credit)
        self.Total_Spending += totalSpending
        return totalSpending
   
    def updateAccounts(self, money, credit):
        self.updateTotalValue(self.updateTotalSpending(money, credit))


    def buyAsset(self, asset_category, asset_name, worth, quantity, payment_mode):
        self.updateTotalValueAdd(worth)
        assetList = list(self.Total_Assets.keys())
      
        if asset_category not in assetList:
            self.Total_Assets[asset_category] = {asset_name : [quantity, worth]}
        else:
            assetsOfCategory = dict(self.Total_Assets[asset_category])
            itemsInAssets = list(assetsOfCategory.keys())
            if asset_name in itemsInAssets:
                new_quantity = assetsOfCategory[asset_name][0] + quantity
                # new_worth = assetsOfCategory[asset_name][1] + worth
            else:
                new_quantity = quantity
                # new_worth = worth
            assetsOfCategory.update({asset_name: [new_quantity, worth]})
            self.Total_Assets[asset_category] = assetsOfCategory

        if payment_mode == 0:
            self.giveMoney(worth)
        elif payment_mode == 1:
            self.giveCredit(worth)

        print("Recieved " + str(asset_name) + " of worth " + str(worth))
        return asset_name, worth
    
    def sellAsset(self, asset_category, asset_name, price, payment_mode):
        assets = self.Total_Assets
        print(assets)
        asset = assets[asset_category]
        asset = asset[asset_name]
        print(asset)
        # self.Total_Assets[asset] = worth
        # if payment_mode == 0:
        #     self.giveMoney(worth)
        # elif payment_mode == 1:
        #     self.giveCredit(worth)

        # print("Recieved " + str(asset) + " of worth " + str(worth))
        return asset

    def getAssetWorth(self):
        print("********************")
        asset_worth_list = list(self.Total_Assets.values())
        print(asset_worth_list)
        asset_worth_items = list(self.Total_Assets.keys())
        return_dict = {}
        print("----------------------------")
        for i in range(len(asset_worth_list)):
            a = list(asset_worth_list[i].values())
            # print(a)
            # for i in range(len(a)):
            #     summ = a[i][0] * a[i][1]
            #     a[i] = summ

            return_dict[asset_worth_items[i]] =  #sum(list(asset_worth_list[i].values()))
        print(a)
        print("----------------------------")

        # totalWorth = sum(list(return_dict.values()))

        # return [totalWorth, return_dict]
          

    def getAccounts(self):
        print("_____________________________________________")
        return_dict = {
            "Spendings" : self.Total_Spending,
            "Value" : self.Total_Value,
            "Money" : self.Total_Money,
            "Credit" : self.Total_Credit,
            "Assets": self.Total_Assets
            # "Unrealized Value" : self.getAssetWorth()[0]
            }
        return return_dict


p1 = Buyer("Hello", 100, 100)
print(p1.getAccounts())
# print(p1.getTotalMoney())
# print(p1.getTotalSpending())
p1.giveMoney(10)
# print(p1.getTotalMoney())
# print(p1.getTotalSpending())
print(p1.getAccounts())
p1.giveMoney(10)
print(p1.getAccounts())
p1.giveMoney(10)
print(p1.getAccounts())
p1.giveMoney(10)
print(p1.getAccounts())
p1.giveMoney(10)
print(p1.getAccounts())
p1.giveMoney(10)
print(p1.getAccounts())
p1.giveMoney(10)
print(p1.getAccounts())
p1.giveMoney(10)
print(p1.getAccounts())
p1.giveMoney(10)
print(p1.getAccounts())
p1.giveMoney(10)
print(p1.getAccounts())


p1.takeMoney(10)
print(p1.getAccounts())
p1.takeMoney(10)
print(p1.getAccounts())
p1.takeMoney(10)
print(p1.getAccounts())
p1.takeMoney(10)
print(p1.getAccounts())
p1.takeMoney(10)
print(p1.getAccounts())
p1.takeMoney(10)
print(p1.getAccounts())
p1.takeMoney(10)
print(p1.getAccounts())
p1.takeMoney(10)
print(p1.getAccounts())
p1.takeMoney(10)
print(p1.getAccounts())
p1.takeMoney(10)
print(p1.getAccounts())


p1.buyAsset("Stocks", "rel_cap", 10, 1, 0)
print(p1.getAccounts())
p1.buyAsset("Stocks", "rel_Infra", 10, 1, 0)
print(p1.getAccounts())
p1.buyAsset("Stocks", "rel_cap", 10, 1, 0)
print(p1.getAccounts())
p1.buyAsset("Stocks", "rel_cap", 10, 1, 0)
print(p1.getAccounts())
p1.buyAsset("Stocks", "rel_cap", 10, 1, 1)
print(p1.getAccounts())
p1.buyAsset("Stocks", "rel", 10, 1, 1)
print(p1.getAccounts())
p1.buyAsset("Stocks", "rel", 10, 1, 1)
print(p1.getAccounts())
p1.buyAsset("Stocks", "rel_Infra", 10, 1, 1)
print(p1.getAccounts())
p1.buyAsset("Stocks", "rel_Infra", 10, 1, 1)
print(p1.getAccounts())
p1.buyAsset("Stocks", "rel_Infra", 10, 1, 1)
print(p1.getAccounts())

p1.buyAsset("Real Estate", "SreeNath Enclave", 500, 1, 0)
print(p1.getAccounts())
p1.buyAsset("Real Estate", "SreeNath Enclave", 500, 1, 0)
print(p1.getAccounts())
p1.buyAsset("Real Estate", "SreeNath Enclave 2", 500, 1, 0)
print(p1.getAccounts())
print(p1.getAssetWorth())
print(p1.Total_Value)

p1.sellAsset("Real Estate", "SreeNath Enclave", 200, 0)


