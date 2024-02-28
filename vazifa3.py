def validate_age(age):
    while True:
        try:
            age = int(age)
            return age
        except ValueError:
            print("Noto'g'ri format! Iltimos, butun son kiriting.")
            age = input("Yoshingizni kiriting: ")

def validate_phone(phone):
    while True:
        if phone.startswith("+998") and len(phone) == 13:
            return phone
        else:
            print("Noto'g'ri format! Iltimos, telefon raqamingizni boshlanishi +998 bilan va 13 ta raqam kiriting.")
            phone = input("Telefon raqamingizni kiriting: ")

def main():
    with open("users_info.txt", "a") as file:
        while True:
            name = input("Ismingizni kiriting: ")
            lastname = input("Familiyangizni kiriting: ")
            age = input("Yoshingizni kiriting: ")
            age = validate_age(age)
            phone = input("Telefon raqamingizni kiriting: ")
            phone = validate_phone(phone)
            email = input("Emailingizni kiriting: ")
            address = input("Manzilingizni kiriting: ")
            user_id = len(open("users_info.txt").readlines()) + 1
            file.write(f"ID: {user_id}, Name: {name}, Lastname: {lastname}, Age: {age}, Phone: {phone}, Email: {email}, Address: {address}\n")
            print("Ma'lumotlar qo'shildi!")
            if input("Yana ma'lumot qo'shasizmi? (ha/yo'q): ").lower() != "ha":
                break

if __name__ == "__main__":
    main()
