import argparse

def main():
    user = {"jhon":"12345"}
    parser = argparse.ArgumentParser(description = 'ID')
    parser.add_argument('username',help = 'username')
    parser.add_argument('password',help = 'password')
    
    arguments = parser.parse_args()


    if arguments.username in user:
        if user[arguments.username] == arguments.password:
            print("Authentication successfull!")
            print(arguments)
            print(type(arguments))

        else:
            print("Password incorrect.")
    else:
        print("Username not found")


if __name__ == "__main__":
    main()  
