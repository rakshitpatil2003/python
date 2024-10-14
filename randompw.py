import random
import string

password_len=12
random_choice = string.ascii_letters + string.digits + string.punctuation

password=""
for i in range(password_len):
    password+=random.choice(random_choice)


print("the randomly generated password is : ",password)