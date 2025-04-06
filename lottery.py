import random

def get_numbers_ticket(min, max, quantity):
     
    if min >= 1 and max <= 1000 and quantity <= max - min + 1:
        return sorted(random.sample(range(min, max + 1), quantity))
    return []



