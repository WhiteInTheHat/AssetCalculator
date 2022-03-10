# Made by Lucas
# All files that are needed
import Bank as B
import Investment as I
import IP
import OA
import Utility as U
import AC
import Report as R

import sys as s



# Keep everything on the bottom
U.clearConsole()
  
  







"""MAIN MENU"""


# This function is used mainly as the menu for what the user would like to do.
def networthFunction(username):
  choice = str(input("What would you like to do: \n (Banking), (Investments), (Investment Portfolio), (Other Assets), (Asset Calculator), (Report), (Logout)\n\n Input: "))

  if choice == "Banking" or choice == "B" or choice == "b":
    U.clearConsole()
    B.bankAccounts(username)
    networthFunction(username)
    
  elif choice == "Investments" or choice == "I" or choice == "i":
    U.clearConsole()
    I.investments(username)
    networthFunction(username)
  
  elif choice == "Investment Portfolio" or choice == "IP" or choice == "ip":
    U.clearConsole()
    IP.investmentPortfolio(username)
    networthFunction(username)
    
  elif choice == "Other Assets" or choice == "OA" or choice == "oa":
    U.clearConsole()
    OA.otherAssets(username)
    networthFunction(username)

  elif choice == "Asset Calculator" or choice == "AC" or choice == "ac":
    U.clearConsole()
    AC.assetCalculator(username)
    networthFunction(username)
  
  elif choice == "Report" or choice == "R" or choice == "r":
    U.clearConsole()
    R.menu(username)
    networthFunction(username)

  elif choice == "Logout" or choice == "L" or choice == "l":
    U.clearConsole()
    End()
  
  else:
    U.clearConsole()
    print("Error ... Please select a valid option!")
    networthFunction(username)




































"""REGISTRATION AND LOGIN SYSTEM"""
# This will allow the user to register an account to the networth calculator system
def Register():
  print("Registraion: ")
  username = str(input("Enter a username: "))
  password = str(input("Enter a password: "))
  password1 = str(input("Confirm your password: "))
  passwordDigit = U.checkDigit(password)
  passwordUpper = U.checkUpper(password)
  usernameExsists = U.alreadyUser(username)
  spacebarCheckU = U.noSpaces(username)
  spacebarCheckP = U.noSpaces(password)


  # Checks if password is the same as the confirmation password
  if password != password1:

    print("Incorrect password, please try again! ")
    Register()
  
  else:
    
    # Forces password to be greater than 6 characters
    if (len(password)) < 6:
      print("Passwrod is too short! ")
      Register()
    # Forces password to contain a digit
    elif passwordDigit == False:
      print("Password does not contain digits! ")
      Register()
    # Forces password to contain at least one uppercase
    elif passwordUpper == False:
      print("Password does not have an uppercase character! ")
      Register()
    # Forces username to be unique
    elif usernameExsists == True:
      print("User already exsists! ")
      Register()
    # Prohibits the use of spacebar characters in username
    elif spacebarCheckU == True:
      print("Spaces used in username! ")
      Register()
    # Prohibits the use of spacebar characters in password
    elif spacebarCheckP == True:
      print("Spaces used in password! ")
      Register()
    # Runs the program as normal and creates all the necessary files for the program to work.
    else:
      f = open("credentials.txt", "a")
      f.write("\n" + username + " " + password + "\n")
      f.close()
      U.clearConsole()
      print("Registration Sucessful...\n")
      fileName1 = "{}'s_Banks.txt".format(username)
      open(fileName1,"x")
      fileName2 = "{}'s_Total_Investment.txt".format(username)
      open(fileName2,"x")
      fileName3 = "{}'s_Investment_Portfolio.txt".format(username)
      open(fileName3,"x")
      fileName4 = "{}'s_Other_Assets.txt".format(username)
      open(fileName4,"x")
      Login(0)
  



# The login system will take in the username and password, it will firstly check if the password is in the database and if it is it will then check if the password linked to that user is correct and allow login to occur if everything checks out.
def Login(num):
  print("Please Log in: ")
  username = str(input("Enter your username: "))
  password = str(input("Enter your password: "))
  passwordx = password + "\n"
  checkUser = U.alreadyUser(username)
  count = num

  tempUsername = U.fetchUsername(username)
  tempPassword = U.fetchPassword(username)
  bool1 = tempUsername == username
  bool2 = tempPassword == passwordx



  if count == 2:
    print("Login has been unsuccessful, please try again later!")
    End()
  elif checkUser == False:
    print("This user does not exsist, go create an account! \n\nPlease try again!")
    count += 1
    Login(count)
  elif bool1 == True and bool2 == True:
    print("Login Successful... Enjoy!\n")
    networthFunction(username)
  else:
    print("Wrong password, please try again!")
    count += 1
    Login(count)


  























"""START FUNCTION"""

# This is how the program actually starts
def Main():
  
  print("Through out this program, there is many times you can choose your own options, you can either type exactly what is inside the brackets OR you can just use the first initial of the thing you want to do.\n\nFor example (Banking) -> b or B or Banking\n\n")
  
  choice = str(input("Register an Account (R) or Login (L): "))
  correctChoice = choice.upper()

  if correctChoice == 'R':
    U.clearConsole()
    Register()
  elif correctChoice == 'L':
    U.clearConsole()
    Login(0)
  else:
    print("Incorrect input, please try again! ")
    Main()















"""END FUNCTION"""

def End():
  print("Logout successful...")
  print("Thanks for using my program!")
  s.exit()




Main()
