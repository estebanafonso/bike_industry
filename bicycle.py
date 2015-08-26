class Bicycle(object):
    def __init__(self,name,weight,cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        
    def getName(self):
        return self.name
        
    def getCost(self):
        return self.cost
       
        
class BikeShop(object):
    def __init__(self,name,margin,inventory):
        self.name = name
        self.margin = margin
        self.inventory = inventory
        self.revenue = 0
        self.profit = 0
    
    def displayRevenue(self):
        print self.name + " has revenue of $" + str(self.revenue)
        
    def displayProfit(self):
        print self.name + " has earned profits of $" + str(self.profit)
        
    def sellBike(self,bike):
        self.revenue += bike.cost*(self.margin+100.0)/100.0
        self.inventory[bike] -= 1
        self.profit += bike.cost*(self.margin+100.0)/100.0 - bike.cost
        
    def displayInventory(self):
        print "Inventory for " + self.name
        for key,value in self.inventory.iteritems():
            print key.getName() + ": " + str(value)
        print "-----------------"
            
    def displayAffordableInventory(self,customer):
        print "Inventory from " + self.name + " that " + customer.getName() + " can afford:"
        for key,value in self.inventory.iteritems():
            if key.getCost() <= customer.getFund():
                print key.getName()
        print "-----------------"
        

        

class Customer(object):
    def __init__(self,name,initial_fund):
        self.name = name
        self.fund = initial_fund
        self.bikes_owned = list()
        
    def buyBike(self, bike, store):
        self.fund -= bike.cost
        self.bikes_owned.append(bike)
        store.sellBike(bike)
        print self.name + " just purchased a " + bike.getName() + " for $" + str(bike.getCost())
        print self.name + " has $" + str(self.fund) + " left in his bike fund."
        
    def displayName(self):
        print "This customer's name is " + self.name
        
    def displayFund(self):
        print self.name + " has $" + str(self.fund)
        
    def displayBikesOwned(self):
        print self.name + " owns " + str([bike.getName() for bike in self.bikes_owned])
        
    def getName(self):
        return self.name
        
    def getFund(self):
        return self.fund
        


