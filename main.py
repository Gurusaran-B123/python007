name = input("enter your name");code=int(input("enter your code"))
match name:
    case " guru":
        if code== 12345:
            print("your this month salary is 25,000")
        else:
            print("wrong code!!!")
    case " sakthi":
        if code== 6789:
            print("your salary credited")
        else:
            print("wrong code or name")
    case _:
        print('who are you???')
