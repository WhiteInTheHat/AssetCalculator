import Utility as U

"""Very Similar to all he functions that take in inputs from the user, this will take in the users bank totals and store it in a file with a grand total of all of the banks"""


# Banking Section
def bankAccounts(username):
  choice = str(input("Would you like to View or Edit your bank statements: \n (View), (Edit) \n\nInput: "))
  
  if choice == "View" or choice == "V" or choice == "v":
    U.clearConsole()
    viewBank(username)
    
  elif choice == "Edit" or choice == "E" or choice == "e":
    U.clearConsole()
    editBank(username)

  else:
    U.clearConsole()
    print("Incorrect input, please try again!")
    bankAccounts(username)



# This just opens the file and reads it
def viewBank(username):
  fileName = "{}'s_Banks.txt".format(username)
  f = open(fileName, "r")
  print(f.read())



# This firstly asks the user how many banks they have so a for loop can be created for that amount of times. It then opens the file in write mode and completely wipes the previous content of the file. It then opens the same file in append plus mode so that the information that the user is inputting can be stored in the file without wiping previous data and also allows for reading to occur at the same time. Lastly to read the actual file what is required is to move th curoser back to the top of the text file by using f.seek(0)
def editBank(username):
  banks = int(input("How many banks do you have? "))
  fileName = "{}'s_Banks.txt".format(username)
  f = open(fileName, "w")
  f.write(username + "'s Accounts': \n")
  total = 0
  f = open(fileName, "a+")
  
  for i in range(banks):
    bank = str(input("Bank name: "))
    account = str(input("Account type: "))
    amount = str(input("Amount: (ONLY THE NUMBER)"))
    intAmount = int(amount)
    total += intAmount
    stringTotal = str(total)

    f.write("("+ bank + ") (" + account + ") \n£ " + amount + "\n\n\n")

  f.write("Total = £ " + stringTotal + "\n\n")
  U.clearConsole()
  f.seek(0)
  print(f.read())