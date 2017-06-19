import random
def listoverlap(list1, list2):
    a = set(list1)
    b = set(list2) 
    return list(a & b)


def main():
    a = [random.randint(0,100) for i in range(10)]
    b = [random.randint(0,100) for i in range(10)]
    print(listoverlap(a,b))


if __name__ == '__main__':
    main()
