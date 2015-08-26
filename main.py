from bicycle import *

def main():

    giant = Bicycle("Giant",10,200)
    trek = Bicycle("Trek",10,400)
    spec = Bicycle("Specialized",10,1000)
    cannon = Bicycle("Cannondale",10,500)
    huffy = Bicycle("Huffy",10,100)
    trike = Bicycle("Trike",10,50)
    
    wheels = BikeShop("Wheels Bike Shop",20,{giant:5,trek:5,spec:2,cannon:2,huffy:2,trike:2})
    
    steve = Customer("Steve",200)
    hank = Customer("Hank",500)
    betsy = Customer("Betsy",1000)
    
    
    
    steve.displayName()
    wheels.displayAffordableInventory(steve)
    
    hank.displayName()
    wheels.displayAffordableInventory(hank)
    
    betsy.displayName()
    wheels.displayAffordableInventory(betsy)
    
    wheels.displayInventory()
    
    steve.buyBike(giant,wheels)
    hank.buyBike(trek,wheels)
    betsy.buyBike(cannon,wheels)
    
    wheels.displayInventory()
    wheels.displayProfit()
    
if __name__ == "__main__":
    main()