import Utility as U

"""Very Similar to all he functions that take in inputs from the user, this will take in the users investment total and store it in a file with a grand total"""

# Investment section:
def investments(username):
  choice = str(input("Would you like to View or Edit your total investments: \n (View), (Edit) \n\nInput: "))
  
  if choice == "View" or choice == "V" or choice == "v":
    U.clearConsole()
    viewInvestment(username)
    
  elif choice == "Edit" or choice == "E" or choice == "e":
    U.clearConsole()
    editInvestment(username)

  else:
    U.clearConsole()
    print("Incorrect input, please try again!")
    investments(username)





def viewInvestment(username):
  fileName = "{}'s_Total_Investment.txt".format(username)
  f = open(fileName, "r")
  print(f.read())





def editInvestment(username):
  totals = int(input("How many investment accounts do you have? "))
  fileName = "{}'s_Total_Investment.txt".format(username)
  f = open(fileName, "w")
  f.write(username + "'s Total Investments: \n\n")
  total = 0
  stringTotal = ""
  f = open(fileName, "a+")
  
  for i in range(totals):

    companyName = str(input("What is the company name holding your investments? "))
    deposited = float(input("How much did you deposit into this account? (ONLY THE NUMBER)"))
    result = float(input("What is the current result? (ONLY THE NUMBER)"))
    actual = (deposited + result)
    stringDeposited = str(deposited)
    stringResult = str(result)
    f.write(companyName + ":\n\n")
    f.write("Total deposited = £ " + stringDeposited + "\n")
    f.write("Current result = £ " + stringResult + "\n\n")
    total += actual

  
  stringTotal = str(total)
  f.write("Total = £ " + stringTotal + "\n\n")
  U.clearConsole()
  f.seek(0)
  print(f.read())