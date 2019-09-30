import datetime


def years(age):
    return (100 - int(age)) + datetime.date.today().year


def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    times = input("How many times? ")
    for i in range(int(times)):
        print("You will be a 100 years old in", years(age))
    return


if __name__ == '__main__':
    main()
