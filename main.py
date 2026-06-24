from register import *
from bank import *

status = False
print("-------------Bank Management System-------------")
while True:
  try:
    register = int(input("1.SIGN-UP\n"
                         "2.SIGN-IN"))
    if register == 1:
      SignUp()
      # f = SignUp()
      # if f == 0:
      #   break
      # f = 1
    elif register == 2:
      user = SignIn()
      status = True
      break
    
    else:
      print("Invalid Choice!!")
  except ValueError:
    print("Enter Numbers Only...")

account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")
# print(account_number[0][0])

while status:
  print(f"Welcome {user.capitalize()} Choose any Banking Services\n")
  try:
    facility = int(input("1.Balance Enquiry\n"
                         "2.Cash Deposit\n"
                         "3.Cash Withdraw\n"
                         "4.Fund Transfer\n"
                         "5.Exit\nEnter Choice: "))
    # if facility >= 1 and facility <= 4:
    match facility:
      case 1:

        bobj = Bank(user,account_number[0][0])
        bobj.balanceenquiry()

      case 2:

        while True:
          try:

            amount = int(input("Enter Amount to deposit: ")) 
            bobj = Bank(user,account_number[0][0])
            bobj.deposit(amount)
            mydb.commit()
            break

          except ValueError:
            print("Enter valid input i.e Number")

      case 3:
        while True:
          try:

            amount = int(input("Enter Amount to withdraw: ")) 
            bobj = Bank(user,account_number[0][0])
            bobj.withdraw(amount)
            mydb.commit()
            break

          except ValueError:
            print("Enter Valid Amount.")

      case 4:

        while True:
          try:

            receive = int(input("Enter Receiver Acc No:"))
            amount = int(input("Enter Money to transfer: ")) 
            bobj = Bank(user,account_number[0][0],receive)
            bobj.fundtransfer(receive,amount)
            mydb.commit()
  
            print("Fund Transfer Successful.")
            break

          except ValueError:
            print("Enter Valid Numeric Input.")

      case 5:
         print("Thank You For Using Bank Management System.")
         status = False

      case _:
        print("Invalid Choice")

  except ValueError:
    print("Invalid Input. Enter Numbers Only.")