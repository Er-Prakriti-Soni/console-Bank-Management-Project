#User registration signin/signup
import random
from customer import *
from bank import Bank

def SignUp():
  username = input("Create Username: ").strip()
  temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
  # print(temp)
  if temp:
    print("Username already exists.")
    return
  print("\nProceed with Registration\n")

    # print("Username available")
  name = input("Enter Name: ")
  mobile = input("Enter Mobile_No: ")
  email = input("Enter Email: ")
  address = input("Enter Address: ")
  aadhar = input("Enter Aadhar No: ")
  # Account Type
  while True:
      try:
          acc_type = int(input(
              "Choose Account Type\n"
              "1. Saving Account\n"
              "2. Current Account\n"
              "Enter Choice: "
          ))

          if acc_type == 1:
              acctype = "Saving Account"
              break

          elif acc_type == 2:
              acctype = "Current Account"
              break

          else:
              print("Invalid Choice!")

      except ValueError:
          print("Enter Numbers Only!")

  # Initial Deposit
  while True:
    try:
        balance = float(input("Enter Initial Deposit (>=2000): "))

        if balance >= 2000:
            break

        print("Minimum balance should be 2000.")

    except ValueError:
        print("Enter Valid Amount.")

  pin = input("Set Password/Passkey: ")
    
  # Generate Unique Account Number
  while True:
      account_number = random.randint(10000000, 99999999)

      temp = db_query(
          f"SELECT account_number FROM customers "
          f"WHERE account_number='{account_number}';"
      )

      if not temp:
          break
    # cobj = Customer(username,password,name,age,city,account_number)
      cobj = Customer(account_number,name,mobile,email,address,aadhar,acctype,balance,pin)
      cobj.createuser()
      bobj = Bank(account_number,name)
      bobj.create_transaction_table()
      print("Account Created Successfully.")

def SignIn():
    print("====== BANK MANAGEMENT SYSTEM ======")
    acc_type = int(input(
              "1. Customer Login\n"
              "2. Admin Login\n"
              "3. Exit\n"
              "Enter Choice: "
          ))
    
    match acc_type:
        case 1:
            while True:
                username = input("Enter Username: ").strip()
                temp = db_query(
                    f"SELECT username FROM customers "
                    f"WHERE username='{username}';"
                )

                if not temp:
                    print("Username does not exist.")
                    continue

                while True:
                    password = input(
                        f"Welcome {username.capitalize()}\n"
                        f"Enter Password: "
                    )

                    temp = db_query(
                        f"SELECT password FROM customers "
                        f"WHERE username='{username}';"
                    )

                    if temp[0][0] == password:
                        print("Sign-In Successful.")
                        return username

                    else:
                        print("Incorrect Password. Try Again.")
        
        case 2:
            pass
        case 3:
            pass
        case _:
            pass