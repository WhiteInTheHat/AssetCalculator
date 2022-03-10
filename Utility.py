"""This Python File will contain just general useful functions used to help bigger functions in the code."""

# Definition required to implement clean slate
clearConsole = lambda: print('\n' * 150)

# This function loops through the user inputs and checks whether the username or the password contains a space in them.
def noSpaces(userinput):
  check = False
  for character in userinput:
    if character == " ":
      check = True


  return(check)


# This function loops through the string and checks if it has an uppercase character.
# This functions recieves the parameter password and uses it as the password in question.
def checkUpper(password):
  check = False
  for character in (password):
    if character.isupper():
      check = True

  
  return(check)


# This function loops through the string and checks if it has a digit.
# This function recieves the parameter password and uses it as the password in question.
def checkDigit(password):
  check = False
  for character in (password):
    if character.isdigit():
      check = True

  
  return (check)



# This function will fetch the username from the line in the text file.
# This function recieves the entire line from the text document and returns the username itself.
def fetchUsername(x):

  username = ""

  for i in x:
    if i == " ":
      break
    else:
      username += i


    
    
  return(username)


# This function will check if the username entered already exsists
# It uses the fetchUsername function to get the username from the first line of the text document. Then compares it to the inputted username.
def alreadyUser(username):
  check = False
  f = open("credentials.txt", "rt")
  for x in f:
    tempUsername = fetchUsername(x)
    if tempUsername == username:
      check = True
  f.close()

  
  return(check)



# This will fetch the password from the credentials file
def fetchPassword(username):
  counter = 0
  tempPassword = ""
  f = open("credentials.txt" , "rt")
  for x in f:
    tempUsername = fetchUsername(x)
    if tempUsername == username:
      for i in x:
        if counter == 1:
          tempPassword += i
        elif i == " ":
          counter += 1
  

  return(tempPassword)

# Converts a list of strings into a list of floats
def floater(list1):

  newList = []

  for i in list1:
    newList.append(float(i))

  return(newList)


