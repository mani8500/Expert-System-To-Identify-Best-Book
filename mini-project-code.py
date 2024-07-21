import sqlite3
conn = sqlite3.connect('mydatabase.sqlite')
cursor = conn.cursor()
print("Opened database successfully")
sql = "DROP TABLE IF EXISTS BOOKSS"

cursor.execute(sql)

cursor.execute('''CREATE TABLE BOOKSS
         (Authrname varchar(100) PRIMARY KEY     NOT NULL,
         bkname          TEXT    NOT NULL,
         rating            INT     NOT NULL,
         edition INT NOT NULL,
         publisher        CHAR(50));''')
cursor.execute("INSERT INTO BOOKSS (Authrname,bkname,rating,edition,publisher) VALUES ('Abraham Silberschatz, Peter Baer Galvin, and Greg Gagne', 'Operating Systems', 4, 7,'Wiley ')");
cursor.execute("INSERT INTO BOOKSS (Authrname,bkname,rating,edition,publisher) VALUES ('William Stallings', 'Operating Systems', 3, 3,'Prentice Hall Software Series ')");
cursor.execute("INSERT INTO BOOKSS (Authrname,bkname,rating,edition,publisher) VALUES ('Andrew S. Tanenbaum', 'Operating Systems', 5, 3,'GOAL Series ')");
cursor.execute("INSERT INTO BOOKSS (Authrname,bkname,rating,edition,publisher) VALUES ('Behrouz A Forouzan', 'Data Communication and Networking', 4, 1,'Vikram')");
cursor.execute("INSERT INTO BOOKSS (Authrname,bkname,rating,edition,publisher) VALUES ('William Stalling', 'Data Communication and Networking', 5,2, 'Vijay')");
cursor.execute("INSERT INTO BOOKSS (Authrname,bkname,rating,edition,publisher) VALUES ('Henry', 'Data Communication and Networking', 5,2, 'Saketh')");
cursor.execute("INSERT INTO BOOKSS (Authrname,bkname,rating,edition,publisher) VALUES ('Marwell', 'Data Communication and Networking', 4,2, 'Praveen')");
cursor.execute("INSERT INTO BOOKSS (Authrname,bkname,rating,edition,publisher) VALUES ('Oriz', 'Data Communication and Networking', 3,2, 'Keerthi')");
cursor.execute("INSERT INTO BOOKSS (Authrname,bkname,rating,edition,publisher) VALUES ('Ivan BayaRoss', 'DBMS', 4,2, 'Vikram')");
cursor.execute("INSERT INTO BOOKSS (Authrname,bkname,rating,edition,publisher) VALUES ('Raghu RamKrishnan', 'DBMS', 5,1, 'Vijay')");
cursor.execute("INSERT INTO BOOKSS (Authrname,bkname,rating,edition,publisher) VALUES ('C.J.Date', 'DBMS', 3,1, 'Rahul')");
cursor.execute("INSERT INTO BOOKSS (Authrname,bkname,rating,edition,publisher) VALUES ('Bipin.C.Desai', 'DBMS', 2,3, 'Lakshman')");
cursor.execute("INSERT INTO BOOKSS (Authrname,bkname,rating,edition,publisher) VALUES ('SilberSchatz', 'DBMS', 1,3, 'Reshma')");

x=0
print("Availabe text books are:\n")
print("1.DBMS\n")
print("2.Data Communication and Networking\n")
print("3.Operating Systems\n")


print("*****enter book name with single quotes*****\n")

n=str(input("Enter the textbook:"))
print("Total books avbl for your required topic:"+n)
m="SELECT * FROM BOOKSS WHERE bkname = {}".format(n)
y=0
for row in cursor.execute(m):
    
    x=x+1
    y=y+1
    print("SNO",y)
    print("Authrname= ", row[0])
    print ("bkname = ", row[1])
    print ("rating= ", row[2])
    print ("edition= ",row[3])
    print ("publisher= ",row[4]), 
    print("\n")
    
print("\n So total books avbl are:"+str(x))
print("\n\n")

print("BEST BOOK BASED ON RATING\n")
m="SELECT * FROM BOOKSS WHERE bkname = {} and rating=(SELECT MAX(rating) from BOOKSS) ".format(n)
for row in cursor.execute(m):
    print("Authrname= ", row[0])
    print ("bkname = ", row[1])
    print ("rating= ", row[2])
    print ("edition= ",row[3])
    print ("publisher= ",row[4]), "\n"
