bidderDict = {}
def addNameToDict():
    name = input("What is your name? ")
    price = input("How much do you want to bid? ")
    bidderDict[name] = price
    more = input("Is there another bidder? yes or no?")
    if more == "yes":
        addNameToDict()
    elif more == "no":
        return bidderDict
    highestBidder = max(bidderDict, key=bidderDict.get)
    
    return f"highest bidder is {highestBidder} with ${bidderDict[highestBidder]}"


    
    
    
print(addNameToDict())
# print(bidderDict)
    
