from numpy import average
import Utility as U


import datetime as dt # Used to get current and past data
import pandas as pd # Used for managing data recieved from the Yahoo Finance website
from pandas_datareader import data as pdr # This is the import required to get all info on stocks (https://github.com/wilsonfreitas/awesome-quant#data-sources) all posible data sources

# Fetch the number of shares the user has for each invested company
def fetchShares(username):
  fileName = "{}'s_Investment_Portfolio.txt".format(username)
  f = open(fileName,"r")
  shareList = []
  betterList = []
  count = 0


  for x in f:

    if count < 3:
      count += 1
      pass
    
    else:
      shares = ""
      spaces = 0
      if x == "":
        pass

      else:

        for i in x:

          if i == " ":
            spaces += 1
          
          elif i == "\n":
            break

          elif spaces == 1:
            shares += i
        shareList.append(shares)

  for share in shareList:
    if share == "":
      pass
    else:
      betterList.append(share)
  
  return(betterList)

# Fetch the average price of all the stocks the user is invested in
def fetchAveragePrice(username):
  fileName = "{}'s_Investment_Portfolio.txt".format(username)
  f = open(fileName,"r")
  priceList = []
  betterList = []
  count = 0


  for x in f:

    if count < 3:
      count += 1
      pass
    
    else:
      stockPrice = ""
      spaces = 0
      if x == "":
        pass

      else:

        for i in x:

          if i == " ":
            spaces += 1
          
          elif i == "\n":
            break

          elif spaces == 3:
            stockPrice += i
        priceList.append(stockPrice)

  for price in priceList:
    if price == "":
      pass
    else:
      betterList.append(price)
  
  
  return(betterList)

# Fetch the list of stocks the user is invested in and put it in an array
def fetchStocks(username):
  
  fileName = "{}'s_Investment_Portfolio.txt".format(username)
  f = open(fileName,"r")
  stockList = []
  count = 0

  for x in f:

    if count < 3:
      count += 1
      pass
    
    else:
      stockName = ""
      if x == "":
        pass

      else:

        for i in x:

          if i == " ":
            break
          
          elif i == "\n":
            pass

          else:
            stockName += i
        stockList.append(stockName)
            
  return(stockList)

# This will use the stock list array to fetch the current value of a stock in dollars and return it in a list
def fetchStockPrice(username):
  end = dt.datetime.now() # This will just set the date and time to the current data and time of your computer
  start = dt.datetime(2000,1,1) # This does not really matter, as long as it is a data

  stockList = fetchStocks(username) # This is a list with the stock names and some random bits and bobs we dont want
  betterList = [] # This will store a better stock name list without the random bits and bobs

  priceArray = [] # This will store the prices of each stock

  # This section of code is used to create the betterList
  for stock in stockList:
    if stock == "":
      pass
    else:
      betterList.append(stock)


  # This wipes the contents of the price file before anything occurs
  f = open("Price.csv", "w")
  f.truncate()
  f.close()
  looper = len(betterList)*2
  
  # This section is what allows us to use the data that has been scraped
  for i in betterList:
    df = pdr.DataReader(i , "yahoo" , start , end)["Adj Close"] # This creates the data frame
    df.tail(1).to_csv("Price.csv" , mode="a", header = True, index = True)  # This will write the data of ONLY the ADJUSTED CLOSE into the Price.csv file 
    dr = pd.read_csv("Price.csv") # This will read the file for the loop below


  # This will get the price for each respective stock
  for i in range(0,looper,2): # A for loop that increments by 2 each time (Skip over the headers)
    tempPrice = dr["Adj Close"][i] # This will get the specfic price in the header
    priceArray.append(tempPrice) # Store the price in the priceArray


  return(priceArray)

  





"""Very Similar to all he functions that take in inputs from the user, this will take in the users investment portfolio"""

def investmentPortfolio(username):
  choice = str(input("Would you like to View or Edit your investment portfolio: \n (View), (Edit) \n\nInput: "))
  
  if choice == "View" or choice == "V" or choice == "v":
    U.clearConsole()
    viewPortfolio(username)
    fetchStockPrice(username)
    
  
  
  elif choice == "Edit" or choice == "E" or choice == "e":
    U.clearConsole()
    editPortfolio(username)

  else:
    U.clearConsole()
    print("Incorrect input, please try again!")
    investmentPortfolio(username)



def viewPortfolio(username):
  fileName = "{}'s_Investment_Portfolio.txt".format(username)
  f = open(fileName, "r")
  print(f.read())

  # This seciton will just calculate the live result for all the stocks from the user
  priceArray = U.floater(fetchStockPrice(username))
  averagePriceArray = U.floater(fetchAveragePrice(username))
  sharesArray = U.floater(fetchShares(username))

  arrayLength = len(priceArray)
  result = 0

  for i in range(arrayLength):

    perShare = (priceArray[i] - averagePriceArray[i])
    tempTotal = (perShare * sharesArray[i])
    result += tempTotal
    
  
  print("Result = $" , round(result,2))




def editPortfolio(username):
  stocks = int(input("How many stocks are you invested in? "))
  fileName = "{}'s_Investment_Portfolio.txt".format(username)
  f = open(fileName, "w")
  f.write(username + "'s Investment Portfolio\n\nStock name|Shares|Price when purchased|Total Invested\n\n")
  f = open(fileName, "a+")


  for i in range(stocks):
    stockName = str(input("What is the Ticker? (MUST BE ACCURATE) "))
    shares = float(input("How many shares do you own in this stock? "))
    averagePrice = float(input("What is your current average price? (ONLY THE NUMBER IN DOLLARS)"))
    total = shares*averagePrice
    strShares = str(shares)
    strPrice = str(averagePrice)
    strTotal = str(total)

    f.write(stockName + " " + strShares + " $ " + strPrice + " $ " + strTotal + "\n\n")

  U.clearConsole()
  f.seek(0)
  print(f.read())
  
