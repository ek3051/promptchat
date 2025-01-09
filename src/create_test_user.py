from database import create_user

if __name__ == "__main__":
    username = input("Enter username: ")
    email = input("Enter email: ")
    create_user(username, email)
    print("Test user created.")
