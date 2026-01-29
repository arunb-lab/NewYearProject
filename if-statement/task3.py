current_users = ['arun','mirak','saugat','akash','nagendra','niroj']
new_users = ['kritesh','puja','sudiksha','basu','arun','mirak']

for new_user in new_users:
    if new_user in current_users:
        print(f"Username'{new_user}' is aleady taken. Please enter a new username.")
    else:
        print(f"Username '{new_user}' is avaliable.")

