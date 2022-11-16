# We've been using built-in functions in Python:

print("Hello")
print(type(5.3))

# We call the print function with the argument "Hello".
# We call the type function with the argument 5.3.

my_list = ['Tyler', 'Adam', 'Abby', 'Michael', 'Joey',
           'Debora', 'Jake', 'Madelyne', 'Aydin', 'Dominic', 'Danny',
           'Roger', 'Cail', 'Patrick', 'Cam', 'Kathleen', 'Shreya',
           'Roshini', 'Miraya', 'Mila', 'Qichao']
# We call the sorted function with the argument my_list.
print(sorted(my_list))

print()


# Now we can define our own functions in Python!

# Define a custom function using the def keyword,
# a name for the function, e.g., blackjack_hand,
# and parentheses
# and a colon (:).
def blackjack_hand():
    player_hand = 20
    dealer_hand = 19
    if (player_hand > dealer_hand) and (player_hand <= 21):
        print("The player wins!")


# To run the function, we call the function:
# blackjack_hand()

print()


def prompt_for_name():
    name = input("What's your name? ")
    print(f"Hello, {name}.")


# prompt_for_name()

print()


def while_with_flag():
    prompt = "\nTell me something, and I'll "
    prompt += "repeat it back to you."
    prompt += "\nEnter 'quit' to end the program. "
    active = True
    while active:
        message = input(prompt)
        if message == 'quit':
            active = False
        else:
            print(message)


# while_with_flag()


# A function can have a changeable part
# called a parameter.
# Give the parameter a NAME in the function definition.
# Put it in the parentheses.
def blackjack_hand2(player_hand):
    dealer_hand = 19
    if (player_hand > dealer_hand) and (player_hand <= 21):
        print("The player wins!")


# Give the parameter a VALUE in the function call.
blackjack_hand2(21)

print()


# The parameter value is called an argument.
# We called blackjack_hand2 with an argument of 21.

def greeting(name):
    print(f'Hello, {name}!')


greeting(input)
greeting('Ryan')

print()


def cheer():
    print('Go Bears!')


cheer()

print()


def cheer2(team_name):
    for i in range(3):
        print(f'Go {team_name}!')


# Cooperating functions.

def main():
    cheer2('Patriots')
    print()
    cheer2('Mets')
    print()
    cheer2('Revs')


# main()

print()


# We've seen functions with zero parameters
# and one parameter.

# We can write functions with more than one parameter.

# The function DEFINITION includes the parameter NAMES
# in the parentheses.
def blackjack_hand3(player_hand, dealer_hand):
    if (player_hand > dealer_hand) and (player_hand <= 21):
        print("The player wins!")


# The function CALL includes the parameter VALUES
# in the parentheses.
blackjack_hand3(21, 15)

# When you use positional arguments 21 and 15,
# Python matches the first argument in the function call 21 with
# the first parameter player_hand in the function
# definition.
# Python matches the second argument  in the function call 15 with
# the second parameter dealer_hand in the function
# definition.

blackjack_hand3(19, 7)

print()


def cheer3(team_name, times):
    for i in range(times):
        print(f'Go {team_name}!'.lower())


# cheer3('Patriots'.upper(), 5)

def main():
    '''Cheer three times for three teams.'''
    for i in range(3):
        print('Go Patriots!')
    print()
    for i in range(3):
        print('Go Mets!')
    print()
    for i in range(3):
        print('Go Revs!')


print()

# main()

unprinted = ['egg timer', 'frog']


def print_models(unprinted, printed):
    """3d print a set of models."""
    while unprinted:
        current_model = unprinted.pop()
        print(f"Printing {current_model}")
        printed.append(current_model)
    print(f'These items are unprinted: {unprinted}')
    print(f'These items were printed: {printed}')


print_models(['phone case', 'pendant', 'ring'], [])

list1 = ['phone case', 'pendant', 'ring']
list2 = []


# if list1:
#   print("Yes!")

# if list2:
#    print("Yes!")

def print_models2(unprinted, printed):
    """3d print a set of models."""
    while unprinted:
        current_model = unprinted.pop()
        print(f"Printing {current_model}")
        printed.append(current_model)
    return printed


printed = print_models2(['phone case', 'pendant', 'ring'], [])
print(printed)

print()


def print3d_batches():
    returned_printed = print_models2(['phone case', 'pendant', 'ring'], [])
    print(print_models2(['egg timer', 'frog'], returned_printed))


print3d_batches()
