# import sqlite3

# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS users
#                   (id INTEGER PRIMARY KEY,
#                    name TEXT,
#                    lastname TEXT,
#                    age INTEGER,
#                    address TEXT,
#                    email TEXT,
#                    phone TEXT)''')

# def add_user():
#     name = input("Ism: ")
#     lastname = input("Familiya: ")
#     age = int(input("Yosh: "))
#     address = input("Manzil: ")
#     email = input("Email: ")
#     phone = input("Telefon raqami: ")
    
#     cursor.execute('''INSERT INTO users (name, lastname, age, address, email, phone)
#                       VALUES (?, ?, ?, ?, ?, ?)''', (name, lastname, age, address, email, phone))
#     conn.commit()

# def save_users_to_db(users):
#     cursor.executemany('INSERT INTO users (name, lastname, age, address, email, phone) VALUES (?,?,?,?,?,?)', users)
#     conn.commit()

# users = [
#     ("Toxir", "Sobirov", 27, "Fergana", "tohir@gmail.com", "+998991234567"),
#     ("Ibrohim", "Aliyev", 32, "Tashkent", "ibrohim@gmail.com", "+998991234599")
# ]
# save_users_to_db(users)

# conn.close()

# -------------------------------------------------------------------------------------------------------------------------
# import csv

# users = []

# def add_user():
#     name = input("Ismingizni kiriting: ")
#     lastname = input("Familyangizni kiriting: ")
#     age = input("Yoshingizni kiriting: ")
#     address = input("Manzilingizni kiriting: ")
#     email = input("Email manzilingizni kiriting: ")
#     phone = input("Telefon raqamingizni kiriting: ")
    
#     user = {
#         "name": name,
#         "lastname": lastname,
#         "age": age,
#         "address": address,
#         "email": email,
#         "phone": phone
#     }
#     users.append(user)

# while True:
#     add_user()
#     stop = input("Dasturni to'xtatish uchun 'stop' deb yozing, davom etish uchun boshqa belgi kiriting: ")
#     if stop.lower() == 'stop':
#         break

# with open('users_info.csv', 'w', newline='') as csvfile:
#     fieldnames = ["name", "lastname", "age", "address", "email", "phone"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     writer.writeheader()
#     for user in users:
#         writer.writerow(user)

# print("Ma'lumotlar fayliga saqlandi: users_info.csv")
