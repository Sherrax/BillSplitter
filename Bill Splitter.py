# write your code here
import random
def number_of_friends():
    number = int(input('Enter the number of friends joining (including you):'))
    if number < 1:
        raise ValueError
    return number


def initialise_dictionary(number):
    print('\nEnter the name of every friend (including you), each on a new line:')
    return {input(): 0 for _ in range(number)}


def add_total_bill():
    print('Enter the total bill value:')
    return int(input())


def split_bill(bill, count_people,is_someone_lucky):
    if(is_someone_lucky) ==0:
        individual_bill = round(bill / count_people, 2)
        for friend in friends_dict:
            friends_dict[friend] = individual_bill
        return friends_dict
    else:
        individual_bill = round(bill / (count_people -1), 2)
        for friend in friends_dict:
            friends_dict[friend] = individual_bill
        friends_dict[is_someone_lucky] = 0
        return friends_dict
def who_is_lucky(friends_dict):
    print('Do you want to use the "Who is lucky?')
    if (input() == 'No'):
        print('No one is going to be lucky')
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
    is_someone_lucky = who_is_lucky(friends_dict)
    print_dict(split_bill(total_bill, friends_count,is_someone_lucky))

except ValueError:
    print('\nNo one is joining for the party')