def palindrome(str):
    text = []
    text2 = []
    for i in str:
        if i != " ":
            text.append(i.lower())
    print(text)
    for i in range(len(text), 0, -1):
        text2.append(text[i - 1])
    if text == text2:
        return True
    else:
        return False
    print(text2)
    


def main():
    text = input("Enter something: ")
    if palindrome(text):
        print("It is a palindrome!")
    else:
        print("It is not a palindrome!")
    
    return


if __name__ == '__main__':
    main()
