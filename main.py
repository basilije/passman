# password manager
# input the information that we want to save
import random
import string
import sqlite3
0
password_list = []


# first time
# import sqlite3
# conn = sqlite3.connect('passwords.db')
# c = conn.cursor()


# c.execute('''CREATE TABLE passwords
#              (website text, username text, password text)''')

# conn.commit()
# conn.close()

import sqlite3
conn = sqlite3.connect('passwords.db')
c = conn.cursor()
aa=c.execute('SELECT * FROM passwords')
aaa = aa.fetchall()
c.close()
for a in aaa:
    password_list.append(dict([("website", a[0]), ("username", a[1]), ("password", a[2]) ]))

while True:
    website = input("What is the website? ")
    username = input("What is the username? ")
    password = input("What is the passsword? ")
    if password == "random":
        try:
            num_of_digits = int(input("How many characters? "))
        except:
            num_of_digits = 16
        random_password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(num_of_digits))
        print(f'This is the random password: {random_password}')
        password = random_password
    else:
        pass

    # print(website)
    # print(username)
    # print(password)

    website_entry = dict([("website", website), ("username", username), ("password", password)])
    # print(website_entry)
    password_list.append(website_entry)

    print(password_list)

    
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()

    # Create table



    c.execute("INSERT INTO passwords VALUES (?,?,?)", [website, username, password])

    conn.commit()
    conn.close()