#Random password generator
import random
import string

x=int(input("Number of caracters : "))
letters=str(input("Letters ? (yes or no) : "))
numbers=str(input("Numbers ? (yes or no) : "))
special_characters=str(input("Special Characters ? (yes or no) : "))

#letters or not
letter=string.ascii_letters
if letters == "yes":
    lettre=letter
else:
    lettre=''


#numbers or not
number=string.digits
if numbers =="yes":
    nombre=number
else:
    nombre=''

#special characters or not
special_character=string.punctuation
if special_characters == "yes":
    caractères_spéciaux=special_character
else:
    caractères_spéciaux=''


#generates password

characters = lettre + nombre + caractères_spéciaux

password = ''.join(random.choice(characters) for i in range(x))
print("Random password is:", password)