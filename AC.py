import Utility as U


"""This function is used to calculate the users assets value grand total, it will look at all the users files and collect a total and return it."""

# A file is opened in read text mode, a for loop is conducted that is the length of the lines in the file f. check variable gets the correct amount of characters that should show Total = £ and then it will check when it pops up. If it pops up it will then store the number next to the text as a float and add return the total.
def fetchTotal(textFile):

  floatNumber = 0.0
  f = open(textFile,"rt")


  
  for x in f:
    check = x[0:10]
    
    if check == "Total = £ ":
      number = x[10:100]
      floatNumber = float(number)

    else:
      pass




    
  return(floatNumber)






# This will get the total from all important files
def assetCalculator(username):
  total = 0
  fileName1 = "{}'s_Banks.txt".format(username)
  total += fetchTotal(fileName1)
  fileName2 = "{}'s_Total_Investment.txt".format(username)
  total += fetchTotal(fileName2)
  fileName4 = "{}'s_Other_Assets.txt".format(username)
  total += fetchTotal(fileName4)
  strTotal = str(total)

  print("Grand Total = £ " + strTotal + "\n\n")