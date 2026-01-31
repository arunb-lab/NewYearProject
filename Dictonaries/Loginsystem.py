import hashlib

users = {}  # username -> hashed_password

def hash_pw(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

while True:
    print("\n1) Register  2) Login  3) Exit")
    ch = input("Choose: ")

    if ch == "1":
        u = input("Username: ").lower()
        if u in users:
            print("Username already exists.")
            continue
        pw = input("Password: ")
        users[u] = hash_pw(pw)
        print("Registered.")

    elif ch == "2":
        u = input("Username: ").lower()
        pw = input("Password: ")
        if users.get(u) == hash_pw(pw):
            print("Login success ✅")
        else:
            print("Invalid login ❌")

    elif ch == "3":
        break
