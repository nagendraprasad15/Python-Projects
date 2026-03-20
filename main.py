from validator import validate_email

def single_email_check():
    email = input("Enter email:")
    if validate_email(email):
        print("✅ valid email")
    else:
        print("❌ Invalid email")


def bulk_email_check():
    try:
        with open("emails.txt", "r") as file:
            emails=file.readlines()

        with open("results.txt","w") as file:
            for email in emails:
                email=email.strip()
                if validate_email(email):
                    file.write(f"{email} -> Valid\n")
                
                else:
                    file.write(f"{email} -> Invalid\n")

                print("results saved in results.txt")
    except FileNotFoundError:
        print(" ❌ emails.txt file not found")



def menu():
    while True:
        print("\n Email validator:")
        print("1. check single email")
        print("2. check bulk emails(from file)")
        print("3. Exit")

        choice = input("enter choice")

        if choice == "1":
            single_email_check()

        elif choice == "2":
            bulk_email_check()

        elif choice == "3":
            print("exiting....")
        



menu()
