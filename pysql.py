import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myuser",
  passwd="mypassword",
  database="superbowl"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM supbowl")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)