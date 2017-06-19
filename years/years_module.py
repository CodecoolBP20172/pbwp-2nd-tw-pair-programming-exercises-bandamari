import datetime


def years(age):
    now = datetime.datetime.now().year
    return (99 - age + now)


def main():
    name = input("What's your name?")
    age = int(input("How old are you?"))
    n = int(input("How many times to print it?"))
    print(("{} will be 100 years old in {}.".format(name,years(age))+"\n") * n)


if __name__ == '__main__':
    main()
