# import os, time
# listOfEmail = []

# while True:
#   print("SPAMMER Inc.")
#   menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
#   elif menu =="2":
#     email = input ("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#   time.sleep(1)
#   os.system("clear")

# import os, time
# listOfEmail = []

# def prettyPrint():
#   os.system("clear") # start by clearing the screen
#   print("listofEmail") # print the title of my program
#   print() # print a blank line
#   for email in listOfEmail: # use for loop to access list
#     print(email)
#   time.sleep(1)

# while True:
#   print("SPAMMER Inc.")
#   menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
#   elif menu =="2":
#     email = input ("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#     prettyPrint()
#   elif menu=="3":
#     os.system("clear")
#     for i in listOfEmail:
#       print("\033[32m",i,"\033[0m")
#     time.sleep(5)
#   time.sleep(1)
#   os.system("clear")

import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear")
  print("listofEmail")
  print()
  for index in range(len(listOfEmail)): # len counts how many items in a list
    print(f"{index}: {listOfEmail[index]}")
  time.sleep(1)

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  time.sleep(1)
  os.system("clear")

# import os, time
# listOfEmail = []

# def prettyPrint():
#   os.system("clear")
#   print("listofEmail")
#   print()
#   for index in range(len(listOfEmail)): # len counts how many items in a list
#     print(f"{index}: {listOfEmail[index]}")
#   time.sleep(1)

# while True:
#   print("SPAMMER Inc.")
#   menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
#   elif menu =="2":
#     email = input ("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#   elif menu == "3":
#     prettyPrint()
#   time.sleep(1)
#   os.system("clear")

# import os, time

# listOfEmail = []

# def prettyPrint():
#   os.system("clear")
#   print("listofEmail")
#   print()

#   for index in range(len(listOfEmail)):
#     print(f"{index}: {listOfEmail[index]}")
#     # counter += 1
#   time.sleep(1)

# while True:
#   print("SPAMMER Inc.")
#   menu = input(
#       "1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
#   elif menu == "2":
#     email = input("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#   elif menu == "3":
#     prettyPrint()
#   time.sleep(1)
#   os.system("clear")

# import os, time

# listOfFood = []

# def prettyPrint():
#   os.system("clear")
#   print("listofFood")
#   print()
#   counter = 1
#   for order in listOfFood:
#     print(f"{counter}: {order}")
#     counter = counter + 1
#   time.sleep(1)

# while True:
#   print("Yummy Food Restaurant")
#   menu = input(
#       "1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
#   if menu == "1":
#     order = input("order > ")
#     listOfFood.append(order)
#   elif menu == "2":
#     order = input("delete order> ")
#     if order in listOfFood:
#       listOfFood.remove(order)
#   elif menu == "3":
#     prettyPrint()
#   time.sleep(1)
#   os.system("clear")

import os, time

listOfFood = []


def prettyPrint():
  os.system("clear")
  print("listofFood")
  print()
  counter = 1
  for order in listOfFood:
    print(f"{counter}: {order}")
    counter += 1
  time.sleep(1)


while True:
  print("Yummy Food Restaurant")
  menu = input(
      "1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
  if menu == "1":
    order = input("order > ")
    listOfFood.append(order)
  elif menu == "2":
    order = input("delete order> ")
    if order in listOfFood:
      listOfFood.remove(order)
  elif menu == "3":
    prettyPrint()
  time.sleep(1)
  os.system("clear")
