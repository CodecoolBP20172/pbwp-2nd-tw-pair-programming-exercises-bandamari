def palindrome(str):
    a = str.replace(" ", "").lower()
    b = str.replace(" ", "").lower()[::-1]
    if a == b:
        return True
    else:
        return False


def main():
    x = input("Enter a palindrome:")
    print(palindrome(x))


if __name__ == '__main__':
    main()
