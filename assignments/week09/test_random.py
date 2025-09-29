import random

def test_random():
    random_number = random.randint(1, 10)

    guess_number = int(input("What is your guess number(1-10)?:"))

    if random_number == guess_number:
        print("Congratulations")
    elif random_number < guess_number:
        print("Too much")
    elif random_number > guess_number:
        print("Too low")

    print(random_number)
    
test_random()