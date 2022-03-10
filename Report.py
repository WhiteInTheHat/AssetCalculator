import Utility as U
import AC
import matplotlib.pyplot as plt
import numpy as np

"""This file is used to allow the user to access all his information to do with his assets in one location"""

def generatePieChart(username):
  
  # This section is used to collect the totals of each section ... Banked, Invested, Other Assets etc.
  fileName1 = "{}'s_Banks.txt".format(username)
  a = AC.fetchTotal(fileName1)
  fileName2 = "{}'s_Total_Investment.txt".format(username)
  b = AC.fetchTotal(fileName2)
  fileName3 = "{}'s_Other_Assets.txt".format(username)
  c = AC.fetchTotal(fileName3)
  
  # We then put this into an array as follows 
  financeChart = np.array([a, b, c])
  # This array will assign a label to each section of the pie chart in chronological order
  mylabels = ["Banked", "Invested", "Other Assets"]


  plt.title("Where Is Your Money") # This function is used to assign a title to the Pie chart
  plt.pie(financeChart, labels = mylabels)
  plt.show() 

def generateBarChart(username):

  # This section is used to collect the totals of each section ... Banked, Invested, Other Assets etc.
  fileName1 = "{}'s_Banks.txt".format(username)
  a = AC.fetchTotal(fileName1)
  fileName2 = "{}'s_Total_Investment.txt".format(username)
  b = AC.fetchTotal(fileName2)
  fileName3 = "{}'s_Other_Assets.txt".format(username)
  c = AC.fetchTotal(fileName3)

  # Two arrays are created, the x-axis array and the y-axis array
  x = np.array(["Banked","Invested","Other Assets"])
  y = np.array([a, b, c])

  # Labels for the title x-axis and y-axis are created
  plt.title("Where Is Your Money")
  plt.xlabel("Location")
  plt.ylabel("Amount (£)")

  # Compiles the x and y arrays together to make the bar chart.
  plt.bar(x,y)
  plt.show()

def graphicalMenu(username):
  choice = str(input("What graphical option would you like to choose? (Bar Chart), (Pie Chart)\n\nInput: "))

  if choice == "Bar Chart" or choice == "BC" or choice == "bc":
    U.clearConsole()
    generateBarChart(username)

  elif choice == "Pie Chart" or choice == "PC" or choice == "pc":
    U.clearConsole()
    generatePieChart(username)

  else:
    U.clearConsole()
    print("Error ... Please select a valid option!")

def report(username): 

  newReportFile = "{}'s_Financial_Report.txt".format(username)
  g = open(newReportFile,"w")
  g.write("")
  g = open(newReportFile,"a")
  




  g.write("---------------------------------------------------------------")

  fileName1 = "{}'s_Banks.txt".format(username)
  a = open(fileName1,"r")
  for x in a:
    g.write(x)

  g.write("---------------------------------------------------------------")

  fileName2 = "{}'s_Total_Investment.txt".format(username)
  b = open(fileName2,"r")
  for x in b:
    g.write(x)

  g.write("---------------------------------------------------------------")

  fileName3 = "{}'s_Investment_Portfolio.txt".format(username)
  c = open(fileName3,"r")
  for x in c:
    g.write(x)

  g.write("---------------------------------------------------------------")

  fileName4 = "{}'s_Other_Assets.txt".format(username)
  d = open(fileName4,"r")
  for x in d:
    g.write(x)

  g.write("---------------------------------------------------------------")

  g = open(newReportFile,"r")
  print(g.read())

  

def menu(username):
  
  choice = str(input("How would you like to see your finances? (Graphical), (Text Report)\n\nInput: "))
  
  if choice == "Graphical" or choice == "G" or choice == "g":
    U.clearConsole()
    graphicalMenu(username)

  elif choice == "Text Report" or choice == "TR" or choice == "tr":
    U.clearConsole()
    report(username)

  else:
    U.clearConsole()
    print("Error ... Please select a valid option!")
    menu(username)



