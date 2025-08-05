
master_pws=input("what is master password? ")
def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data=line.strip()
            user,passw=data.split(" ")
            print("User:",user," Password:",passw)


def add():
    name=input("Account name: ")
    pwd=input("Password: ")

    with open("password.txt","a") as f:
        f.write(name + " " + pwd + "\n")


while True:
    mode = input("would you like to add a new password or view existing one?press q to to exist.").lower()
    if mode=="q":
        break
    if mode=="view":
        view()

    elif mode=="add":
        add()
    else:
        print("Invalid mode. ")
        continue
