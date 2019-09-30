import random

def passwordgen(strength):
    valid_password=[0, 0, 0, 0]
    password = []
    length = 0
    words = ["dog", "asd123", "lol", "sajt"]
    numbers = [str(i) for i in range(0,10)]
    letters_lower = [chr(i) for i in range(97, 123)]
    letters_upper = [chr(i) for i in range(65, 91)]
    symbols = [chr(i) for i in range(33, 48)]
    if strength == "1":
        return words[random.randrange(0, len(words))]
    elif strength == "2":
        length = random.randrange(5, 10)
        valid_password=[0, 0, 0, 1]
    elif strength == "3":
        length = random.randrange(10, 20)
        valid_password=[0, 0, 0, 0]
    print(length)
    while valid_password!=[1,1,1,1] and len(password) != length:
        password = []
        for i in range(length):
            rand = random.randrange(0, int(strength) + 1)
            if rand == 0:
                password.append(numbers[random.randrange(0, len(numbers))])
                valid_password[0]=1
            elif rand == 1:
                password.append(letters_lower[random.randrange(0, len(letters_lower))])
                valid_password[1]=1
            elif rand == 2:
                password.append(letters_upper[random.randrange(0, len(letters_upper))])
                valid_password[2]=1
            elif rand == 3 and strength == "3":
                password.append(symbols[random.randrange(0, len(symbols))])
                valid_password[3]=1
        #print(numbers)
    
    #print(symbols)
    print(len(password))
    return "".join(password)


def main():
    accepted = False
    while not accepted:
        strength = input("How strong password do you need? (1-weak, 2-normal, 3-strong) ")
        if strength == "1" or strength == "2" or strength == "3":
            accepted = True
    print(passwordgen(strength))
    return


if __name__ == '__main__':
    main()
