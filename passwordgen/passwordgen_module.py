import random, string

def passwordgen():
   return ''.join(random.choice(string.ascii_letters + string.digits + '!@#$%^&*()') for i in range(8))


def main():
    l = ["cicuka", "kutyika", "mókuska", "békuci"]
    while True:
        password = input("Do you want a random password(Y/N)?")
        if password.lower() == "y":
            password_level = input("Do you want a strong password(Y/N)?")
            if password_level.lower() == "y":
                print (passwordgen())
            else:
                print (random.choice(l))

            continue
        else:
            break


if __name__ == '__main__':
    main()
