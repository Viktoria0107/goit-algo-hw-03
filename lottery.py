import random

def get_numbers_ticket(min, max, quantity):
    list_lottery_numbers = [] 
    if min >= 1 and max <= 1000:
        list_lottery_numbers.append(sorted(random.sample(range(min, max + 1), quantity)))
    return list_lottery_numbers
    

