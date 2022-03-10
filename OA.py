import Utility as U


"""Very Similar to all he functions that take in inputs from the user, this will take in other assets that may not fit in with other characteristics and store it in a text file with a grand total at the end"""

def otherAssets(username):
  choice = str(input("Would you like to View or Edit your investment portfolio: \n (View), (Edit) \n\nInput: "))
  
  if choice == "View" or choice == "V" or choice == "v":
    U.clearConsole()
    viewOtherAssets(username)
    
  
  elif choice == "Edit" or choice == "E" or choice == "e":
    U.clearConsole()
    editOtherAssets(username)

  else:
    U.clearConsole()
    print("Incorrect input, please try again!")
    otherAssets(username)


    

def viewOtherAssets(username):
  fileName = "{}'s_Other_Assets.txt".format(username)
  f = open(fileName, "r")
  print(f.read())



  

def editOtherAssets(username):
  totalAssets = int(input("How many other assets do you have? "))
  fileName = "{}'s_Other_Assets.txt".format(username)
  f = open(fileName, "w")
  f.write(username + "'s Other Assets\n\n")
  f = open(fileName, "a+")
  total = 0

  for i in range(totalAssets):
    assetName = str(input("What is the name of the asset? "))
    price = int(input("What is the price of the asset? (ONLY THE NUMBER)"))
    strPrice = str(price)
    f.write(assetName + "| £ " + strPrice + "\n")
    total += price

  strTotal = str(total)
  f.write("\nTotal = £ " + strTotal + "\n\n") 
  U.clearConsole()
  f.seek(0)
  print(f.read())
