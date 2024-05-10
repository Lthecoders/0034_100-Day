import os, time

listOfEmail = []


def prettyPrint():
  os.system("clear")
  print("listofEmail")
  print()
  for index in range(len(listOfEmail)):  # len counts how many items in a list
    print(f"{index}: {listOfEmail[index]}")
  time.sleep(1)


while True:
  print("SPAMMER Inc.")
  menu = input(
      "1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu == "2":
    email = input("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    #give me an random email and give and also two paragraphs messages
    print("Spamming...\n\n\n")
    email = [
        "employee1@office.com",
        "employee2@office.com",
        "employee3@office.com",
        "employee4@office.com",
        "employee5@office.com",
        "employee6@office.com",
        "employee7@office.com",
        "employee8@office.com",
        "employee9@office.com",
        "employee10@office.com",
    ]

    print("Spamming...\n\n")
    print(
        f"""{email[0]}\n\nWe are planning a major overhaul of our current project management system. The new system will be more efficient and user-friendly, allowing us to track our projects more effectively."""
    )
    time.sleep(5)
    os.system("cls")
    #different contnet in email and not the same
    print("Spamming...\n\n")
    print(
        f"""{email[1]}\n\nThe upcoming team building event is designed to foster better communication and collaboration among team members. We believe that this will lead to improved performance and productivity.."""
    )
    time.sleep(5)
    os.system("cls")
    print("Spamming...\n\n")
    print(
        f"""{email[2]}\n\nWe are pleased to announce that we have secured a new client for our company. This is a major win for us and we are excited to work with them on their upcoming projects."""
    )
    time.sleep(5)
    os.system("cls")
    print("Spamming...\n\n")
    print(
        f"""{email[3]}\n\nWe are currently looking for a new team member to join our team. The ideal candidate will have experience in project management and be able to work well under pressure."""
    )
    time.sleep(5)
    os.system("cls")
    print("Spamming...\n\n")
    print(
        f"""{email[4]}\n\nWe are pleased to announce that we have secured a new client for our company. This is a major win for us and we are excited to work with them on their upcoming projects."""
    )
    time.sleep(5)
    os.system("cls")
    print("Spamming...\n\n")
    print(
        f"""{email[5]}\n\nWe are currently looking for a new team member to join our team. The ideal candidate will have experience in project management and be able to work well under pressure."""
    )
    time.sleep(5)
    os.system("cls")
    print("Spamming...\n\n")
    print(
        f"""{email[6]}\n\nWe are in the process of updating our office policies. The updated policies will be shared with all employees and will come into effect from next month."""
    )
    time.sleep(5)
    os.system("cls")
    print("Spamming...\n\n")
    print(
        f"""{email[7]}\n\nWe are currently looking for a new team member to join our team. The ideal candidate will have experience in project management and be able to work well under pressure."""
    )
    time.sleep(5)
    os.system("cls")
    print("Spamming...\n\n")
    print(
        f"""{email[8]}\n\nhe upcoming training session will focus on improving our technical skills. This will help us stay up-to-date with the latest industry trends and technologies."""
    )
    time.sleep(5)
    os.system("cls")
    print("Spamming...\n\n")
    print(
        f"""{email[9]}\n\nWe are launching a new initiative to improve our customer service. This will involve training sessions and workshops for all customer service employees."."""
    )
    time.sleep(5)
    os.system("cls")
    print("\n\nDone!")
  time.sleep(1)
  os.system("clear")
