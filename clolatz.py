def collatz(number):
    if number%2==0:
        number=number//2
        print(number)
    else:
        number=number*3+1
        print(number)
    return number


def main():
    try:
        number=int(input("please input a number:"))
    except ValueError as identifier:
        print(identifier)
        print("you should input a number rather a letter or a sentence")
        print("reset your numbe as 1")
        number=1
    print()
    result=collatz(number)
    while True:
        if result!=1:
            result=collatz(result)
        else:
            break
main()

  