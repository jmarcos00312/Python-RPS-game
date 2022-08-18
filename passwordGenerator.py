import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my password generator project")
passwordlen = int(input("How many characters do you want on this password? "))
numberslen = int(input("How many numbers do you want? "))
symbolslen = int(input("How many symbols do you want? "))
letterslen = passwordlen - numberslen - symbolslen

generatedPassword = []

for x in range(letterslen):
    generatedPassword.append(random.choice(letters))
for x in range(symbolslen):
    generatedPassword.append(random.choice(symbols))
for x in range(numberslen):
    generatedPassword.append(random.choice(numbers))
    
random.shuffle(generatedPassword)
genChar = ''.join(generatedPassword)

print(genChar)
