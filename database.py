import mysql.connector as sql

mydb = sql.connect(
  host="localhost",
  user="root",
  password="2307dkps",
  database="bank"
)
cursor = mydb.cursor()

def db_query(str):
  cursor.execute(str)
  result = cursor.fetchall()
  return result

def createcustomertable():
  db_query('''
        CREATE TABLE IF NOT EXISTS customers  
        (acc_no INT PRIMARY KEY NOT NULL,
        name VARCHAR(50) NOT NULL,
        mobile VARCHAR(15) NOT NULL,
        email VARCHAR(50) NOT NULL,
        address VARCHAR(100) NOT NULL,
        aadhar VARCHAR(20) NOT NULL,
        acc_type VARCHAR(20) NOT NULL,
        balance FLOAT NOT NULL,
        pin VARCHAR(20) NOT NULL,
        status BOOLEAN NOT NULL)
  ''')

mydb.commit()

if __name__ == "__main__":
  createcustomertable()
