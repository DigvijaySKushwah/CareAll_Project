import sqlite3

db = sqlite3.connect('careall.db')
cursor = db.cursor()



class young:
    def send_request(self, k):
        sql = "SELECT Id,Name,Age,Fund_raised,Contact,Review,Rating FROM elder_details Where Taken_care_by=0;"
        cursor.execute(sql)
        row = list(cursor.fetchall())
        print("Following is the list of registered Elders")
        for i in row:
            print(i)
        j = input("Enter Id of the elder to want to take care of = ")
        sq = 'UPDATE elder_details SET Request_id' + '="' + k + '" WHERE Id' + '="' + j + '";'
        cursor.execute(sq)
        db.commit()
        print("Response send successfully")

    def login(self, n):
        sql = "SELECT * FROM youth_details Where Id = " + n + ";"
        cursor.execute(sql)
        row = list(cursor.fetchone())
        print("id :", row[0])
        print("Name :", row[1])
        print("Age :", row[2])
        print("Address :", row[3])
        print("Contact :", row[4])
        print("Number of undertaken elders :", row[5])
        print("Review :", row[6])
        print("Rating :", row[7])
        i = input("1. To send request to elders \n 2. To give review \n")
        if i == "1":
            yg.send_request(n)
        elif i == "2":
            j = input("Enter the id of elder")
            rr.young_review_and_rating(j)
        else:
            print("Please enter a valid response")

    def signup(self, i, j, l, k,m):
        sql = "INSERT INTO youth_details(Id,Name,Age,Address,Contact) VALUES (?,?,?,?,?)"
        val = (i,str(j), l, k,m)
        cursor.execute(sql, val)
        db.commit()
        sq = "SELECT Id FROM youth_details Where Contact" + "=" + str(m) + ";"
        cursor.execute(sq)
        i = list(cursor.fetchone())
        print("Signup successful, your Login Id is ", i[0])


class review_and_rating:

    def young_review_and_rating(self, k):
        i, j = input("Enter Reviews = "), input("Enter Rating = ")
        sql = 'UPDATE elder_details SET Review ' + '="' + str(i) + '", Rating ' + '="' + str(
            j) + '" WHERE Id' + '="' + k + '";'
        cursor.execute(sql)

    def elder_review_and_rating(self, k):
        i, j = input("Enter Reviews = "), input("Enter Rating = ")
        sql = 'UPDATE youth_details SET Review ' + '="' + str(i) + '", Rating ' + '="' + str(
            j) + '" WHERE Id' + '="' + k + '";'
        cursor.execute(sql)


class elder:

    def confirm_request(self, k):
        sql = "SELECT Request_id FROM elder_details Where Id" + "=" + k + ";"
        cursor.execute(sql)
        row = list(cursor.fetchone())
        sq = 'SELECT Id,Name,Address,Contact FROM youth_details Where Id = "' + str(row[0]) + '";'
        cursor.execute(sq)
        row1 = list(cursor.fetchone())
        print("Id :", row1[0])
        print("Name :", row1[1])
        print("Address :", row1[2])
        print("Contact :", row1[3])
        i = (input("Press C to confirm or Press R to reject = ")).lower()
        if i == "c":
            sql1 = 'UPDATE elder_details SET Request_id' + '="' + str(0) + '", Taken_care_by' + '="' + str(
                row[0]) + '" WHERE Id' + '="' + k + '";'
            cursor.execute(sql1)
            sql2 = 'UPDATE youth_details SET Number_undertaken_elders = Number_undertaken_elders+1 Where Id ' + '="' + str(
                row[0]) + '";'
            cursor.execute(sql2)
            sql3 = sql = "INSERT INTO taking_care(youth_id,old_id_1) VALUES (%s, %s)"
            val = (str(row[0]), k)
            cursor.execute(sql3, val)
            db.commit()
            print("Confirmed")
        elif i == "r":
            sql4 = 'UPDATE elder_details SET Request_id' + '="' + str(0) + '" WHERE Id' + '="' + k + '";'
            cursor.execute(sql4)
            db.commit()
            print("Rejected")

    def login(self, n):
        sql = "SELECT Id,Name,Age,Fund_raised,Contact,Taken_care_by,Review,Rating FROM elder_details Where Id = " + n + ";"
        cursor.execute(sql)
        row = list(cursor.fetchone())
        print("id :", row[0])
        print("Name :", row[1])
        print("Age :", row[2])
        print("Fund_raised :", row[3])
        print("Contact :", row[4])
        print("Taken_Care_By :", row[5])
        print("Review :", row[6])
        print("Rating :", row[7])

        i =input("1. To Confirm pending request \n 2. To give review \n")
        if i == "1":
            ed.confirm_request(n)
        elif i == "2":
            j = input("Enter the id of youth")
            rr.elder_review_and_rating(j)
        else:
            print("Please enter a valid response")

    def signup(self, i, j, l, k,m):
        sql = "INSERT INTO elder_details(Id,Name,Age,Fund_raised,Contact) VALUES (?,?,?,?,?)"
        val = (i,str(j), l, k, m)
        cursor.execute(sql, val)
        db.commit()
        sq = "SELECT Id FROM elder_details Where Contact" + "=" + str(m) + ";"
        cursor.execute(sq)
        i = list(cursor.fetchone())
        print("Signup successfull, your Login Id is ", i[0])




ed = elder()
yg = young()
rr = review_and_rating()
a = (input("Please enter weather you are elder or young = ")).lower()
if  a == "elder" :
    b = input("Login or Signup = ")
    if b == "login" or b == "Login" or b == "LOGIN":
        old_id = input("Enter your id = ")
        ed.login(old_id)
    elif b == "Signup" or b == "signup" or b == "SIGNUP":
        id,name, age, fund_raised, contact = input("Enter Id= "),input("Enter name= "), int(input("Enter age where age>50 = ")), int(
            input("Fund raised per month in RS.= ")), int(input("Enter mobile number = "))
        ed.signup(id,name, age, fund_raised, contact)
    else:
        print("Please enter a valid response")
elif a == "young":
    b = (input("Login or Signup = ")).lower()
    if b == "login":
        young_id = input("Enter id  = ")
        yg.login(young_id)
    elif b == "signup":
        id,name, age, address, contact =input("Enter Id= "),input("Enter name = "), int(input("Enter age where 25>age<40 = ")), input(
            "Enter your complete address = "), int(input("Enter mobile number = "))
        yg.signup(id,name, age, address, contact)
else:
    print("Invalid")