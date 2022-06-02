import os

clear = lambda: os.system('cls')

nums = [1, 2, 3, 4, 5]

print('\nLaço 1:\n')

for num in nums:
    if num == 4:
        print("Found")
        break # Break interromp o laço
    elif num == 2:
        continue # Continue pula um passo da iteração
    print(num)

print('\nLaço 2:\n')

for num in nums:
    for letter in 'abc':
        print(num, letter)

print('\nLaço 3:\n')

for i in range(1,10):
    print(i)

x = 0

print('\nLaço 4:\n')

while x != 10:
    x += 1
    print(x)