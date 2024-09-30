import csv

# # Import pyodbc to connect to SQL Server database
import pyodbc 

# Building connection string to the database

conn_str = (
    r'driver={ODBC Driver 18 for SQL Server};'
    r'server=(local);'
    r'database=Scrapy;'
    r'trusted_connection=yes;'
    r'TrustServerCertificate=yes;'
    )

# Connection to the database

cnxn = pyodbc.connect(conn_str)

# Use to execute sql queries

cursor = cnxn.cursor()

# Opening the CSV file from the specified path

with open("C:/Users/Firat/Desktop/Scrapy/skrapning_v3_cleaned.csv", "r",  encoding="utf-8") as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        cursor.execute("INSERT INTO CarData(Company,Location,Year,Fuel,Miles,Gear,Price,Name,Brand,Model,EngineVolume,Horsepower) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6],lines[7],lines[8],lines[9],lines[10],lines[11]))

# Committing the changes to the database

cnxn.commit()

# Closing the database connection

cnxn.close()


print("Loaded into database!")