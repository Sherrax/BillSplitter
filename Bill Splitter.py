import random
def number_of_friends():
    number = int(input('Enter the number of friends joining (including you): '))
    if number < 1:
        raise ValueError("Number of friends must be at least 1.")
    return number

def initialise_dictionary(number):
    print('\nEnter the name of every friend (including you), each on a new line:')
    return {input(): 0 for _ in range(number)}

def add_total_bill():
    print('Enter the total bill value:')
    return int(input())

def split_bill(bill, count_people, lucky_friend):
    if lucky_friend == 0:
        individual_bill = round(bill / count_people, 2)
        for friend in friends_dict:
            friends_dict[friend] = individual_bill
    else:
        individual_bill = round(bill / (count_people - 1), 2)
        for friend in friends_dict:
            friends_dict[friend] = individual_bill
        friends_dict[lucky_friend] = 0
    
    return friends_dict

def who_is_lucky(friends_dict):
    print('Do you want to use the "Who is lucky?" feature? (Yes/No)')
    if input().strip().lower() == 'no':
        print('No one is going to be lucky.')
        return 0
    else:
        random_key = random.choice(list(friends_dict))
        print('{} is the lucky one!'.format(random_key))
        return random_key

def print_dict(dictionary):
    print(dictionary)

try:
    friends_count = number_of_friends()
    friends_dict = initialise_dictionary(friends_count)
    total_bill = add_total_bill()
    lucky_friend = who_is_lucky(friends_dict)
    print_dict(split_bill(total_bill, friends_count, lucky_friend))

except ValueError as e:
    print(f'\nError: {e}')
