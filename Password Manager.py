import json
import os
import hashlib

PASSWORD_FILE = "passwords.json"
MASTER_FILE = "master.txt"

# 🔐 Hash the password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# 🛠 First-time setup for master password
def set_master_password():
    print("🔐 First-time setup: Create a Master Password.")
    password = input("Enter new master password: ")
    confirm = input("Confirm password: ")
    if password != confirm:
        print("❌ Passwords do not match. Try again.\n")
        set_master_password()
    else:
        hashed = hash_password(password)
        with open(MASTER_FILE, "w") as f:
            f.write(hashed)
        print("✅ Master password set successfully.\n")

# 🔒 Verify entered master password
def verify_master_password():
    if not os.path.exists(MASTER_FILE):
        set_master_password()

    with open(MASTER_FILE, "r") as f:
        saved_password = f.read()

    entered_password = input("Enter Master Password: ")
    hashed_entered = hash_password(entered_password)
    if hashed_entered != saved_password:
        print("❌ Incorrect password. Access denied.")
        exit()
    print("✅ Access granted.\n")

# 📂 Load saved credentials
def load_passwords():
    if not os.path.exists(PASSWORD_FILE):
        return []
    with open(PASSWORD_FILE, "r") as file:
        return json.load(file)

# 💾 Save updated credentials
def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

# ➕ Add a new entry
def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    credentials = {
        "website": website,
        "username": username,
        "password": password
    }

    data = load_passwords()
    data.append(credentials)
    save_passwords(data)
    print("✅ Password added successfully.\n")

# 📃 View all saved credentials
def view_passwords():
    data = load_passwords()
    if not data:
        print("No passwords saved yet.\n")
        return
    print("\n🔐 Saved Credentials:")
    for i, entry in enumerate(data, start=1):
        print(f"{i}. Website: {entry['website']} | Username: {entry['username']} | Password: {entry['password']}")
    print()

def update_password():
    data = load_passwords()
    if not data:
        print("No passwords to update.\n")
        return

    print("\n✏️ Stored Passwords:")
    for i, entry in enumerate(data, start=1):
        print(f"{i}. Website: {entry['website']} | Username: {entry['username']} | Password: {entry['password']}")

    try:
        index = int(input("Enter the number of the entry to update: "))
        if 1 <= index <= len(data):
            entry = data[index - 1]
            print("\nWhat would you like to update?")
            print("1. Website")
            print("2. Username")
            print("3. Password")
            field_choice = input("Choose a field (1-3): ")

            if field_choice == "1":
                new_website = input("Enter new website: ")
                entry["website"] = new_website
            elif field_choice == "2":
                new_username = input("Enter new username: ")
                entry["username"] = new_username
            elif field_choice == "3":
                new_password = input("Enter new password: ")
                entry["password"] = new_password
            else:
                print("❌ Invalid option.\n")
                return

            save_passwords(data)
            print("✅ Password entry updated successfully.\n")
        else:
            print("❌ Invalid entry number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def delete_password():
    data = load_passwords()
    if not data:
        print("No passwords to delete.\n")
        return
    
    print("\n🗑️ Stored Passwords:")
    for i, entry in enumerate(data, start=1):
        print(f"{i}. Website: {entry['website']} | Username: {entry['username']}")

    try:
        index = int(input("Enter the number of the entry to delete: "))
        if 1 <= index <= len(data):
            removed = data.pop(index - 1)
            save_passwords(data)
            print(f"✅ Deleted entry for {removed['website']}.\n")
        else:
            print("❌ Invalid entry number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# 🔍 Search credentials by website
def search_password():
    keyword = input("Enter website to search: ").lower()
    data = load_passwords()
    found = [entry for entry in data if keyword in entry['website'].lower()]
    
    if found:
        print("\n🔍 Search Results:")
        for entry in found:
            print(f"Website: {entry['website']} | Username: {entry['username']} | Password: {entry['password']}")
    else:
        print("No matching entries found.")
    print()

# 🧭 Main menu loop
def menu():
    while True:
        print("==== Password Manager ====")
        print("1. Add Password")
        print("2. View All Passwords")
        print("3. Search Password by Website")
        print("4. Delete a Password")
        print("5. Update a Password")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            update_password()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

# 🏁 Run the app
if __name__ == "__main__":
    verify_master_password()
    menu()
