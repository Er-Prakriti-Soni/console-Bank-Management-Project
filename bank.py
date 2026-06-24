#Bank Services
from database import *
import datetime

class Bank:
  def __init__(self,account_number,username):
    self.__account_number = account_number
    self.__username = username
    self.create_transaction_table()
  
  def create_transaction_table(self):
    db_query(f'''CREATE TABLE IF NOT EXISTS transaction_{self.__account_number} (
             tid INT AUTO_INCREMENT PRIMARY KEY,
             acc_no INT,
             ttype VARCHAR(20),
             tdate VARCHAR(30),
             amount FLOAT,
             FOREIGN KEY (acc_no) REFERENCES customers(acc_no)
             )''')
    
  def balanceenquiry(self):
    temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
    print(f"{self.__username} Balance:{temp[0][0]}")

  def deposit(self,amount):
    temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
    # print(temp[0][0])
    test = amount + temp[0][0]
    db_query(f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}';")
    self.balanceenquiry()
    db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
             f"'{self.__account_number}',"
             f"'Deposit',"
             f"'{amount}',"
             f"'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'"
             f")")
    print(f"{self.__username} Successfully Deposited : {self.__account_number}")
  
  def withdraw(self,amount):
    temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
    # print(temp[0][0])
    if amount > temp[0][0]:
      print("Insufficient Balance please deposit money")
    else:
      test = temp[0][0] - amount
      db_query(f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}';")
      self.balanceenquiry()
      db_query(f"INSERT INTO transaction_{self.__account_number} VALUES ("
              f"'{self.__account_number}',"
              f"'Withdraw',"
              f"'{amount}',"
              f"'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'"
              f")")
      print(f"{self.__username} Successfully Withdrawn : {self.__account_number}")

  def fundtransfer(self,receive,amount):
    temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
    # print(temp[0][0])
    if amount > temp[0][0]:
      print("Insufficient Balance. Please deposit money first")
      return
    
    temp2 = db_query(f"SELECT balance FROM customers WHERE acc_no = '{receive}';")
    test1 = temp[0][0] - amount
    test2 = temp2[0][0] + amount
    db_query(f"UPDATE customers SET balance = '{test1}' WHERE name = '{self.__username}';")
    db_query(f"UPDATE customers SET balance = '{test2}' WHERE acc_no = '{receive}';")
    receiver_username = db_query(f"SELECT name FROM customers WHERE acc_no = '{receive}';")
    self.balanceenquiry()
    db_query(f"""INSERT INTO {receiver_username[0][0]}_transaction VALUES (
            {self.__account_number},
            'Fund Received From <<{self.__account_number}',
            {amount},
            {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            )""")
    db_query(f"""INSERT INTO {self.__username}_transaction VALUES (
            {self.__account_number},
            'Fund Transfer To <<{receive}',
            {amount},
            {datetime.datetime.now()}
            )""")
    print(f"{self.__username} Amount is successfully transaction from your account {self.__account_number}")
