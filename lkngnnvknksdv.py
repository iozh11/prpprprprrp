import random

a, b = map(float, input().split())
random_numbers = []
while len(random_numbers) != 5:
    number = random.uniform(a, b)
    if number != b:
        random_numbers.append(number)

for i in random_numbers:    
    print("{:.3f}".format(i), end=" ")