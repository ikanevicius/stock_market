def get_float(input_question):
    """Ask for user input and checks if user input is a float.
    If The input is incorrect, the function returns 'None'."""

    user_input = input(input_question)
    user_input = user_input.replace(' ', '')
    user_input = user_input.replace(',', '.')

    if user_input.count(".") > 1:
        print("ERROR. Can`t use more than one dot to separate decimals.")
        return None

    numbers = []
    for i in user_input:
        if i.isnumeric() or i == ".":
            numbers.append(i)
        else:
            continue

    if len(numbers) != len(user_input):
        print("ERROR. Input must be a number.")
        return None

    user_input = float(user_input)
    user_input = round(user_input, 3)

    return user_input


def get_integer(input_question):
    """Ask for user input and checks if user input is an integer.
    If The input is incorrect, the function returns 'None'."""

    user_input = input(input_question)
    user_input = user_input.replace(' ', '')

    if user_input.isnumeric():
        user_input = int(user_input)
        return user_input
    else:
        print("ERROR. Input must be a number and can`t have decimals.")
        return None
