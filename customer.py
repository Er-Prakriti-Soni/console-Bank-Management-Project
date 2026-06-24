#Customer Details
from database import *

class Customer:
  def __init__(self,account_number,name,mobile,email,address,aadhar,acctype,balance,pin):
    self.__account_number = account_number
    self.__username = name
    self.__mobile = mobile
    self.__email = email
    self.__address = address
    self.__aadhar = aadhar
    self.__acctype = acctype
    self.__balance = balance
    self.__password = pin


  def createuser(self):
    temp = db_query(f'''INSERT INTO customers VALUES (
                    '{self.__account_number}',
                    '{self.__username}',
                    '{self.__mobile}',
                    '{self.__email}',
                    '{self.__address}',
                    '{self.__aadhar}',
                    '{self.__acctype}',
                    '{self.__balance}',
                    '{self.__password}',
                    1
                    );
                    ''')
    mydb.commit()