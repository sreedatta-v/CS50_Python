def is_forty_two(user_input):
    user_input = user_input.lower().strip()

    return ( user_input == "42" or
             user_input == "forty-two" or
             user_input == "forty two")

user_input = input("What's the input? ")

if is_forty_two(user_input):
    print("Yes")
else:
    print("No")