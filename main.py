import random
import string
# password manager

password_list = []

def new_password():
    website = input('What is the website? ')
    username = input('What is the username? ')
    password = input('What is the password? ')
    if password == 'random':
        num_of_digits = int(input('How many characters long should the password be? '))
        random_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(num_of_digits))
        print(f'This is the random password: {random_password}')
        password = random_password
    else:
        pass
    
    website_entry = dict([("website", website), ("username", username), ("password", password)]) 
    password_list.append(website_entry)
    print(password_list)

while True:
    print('''
    Welcome to the password manager ya dingus.
    Type "new" to create a new password.
    Type "show" to look up a password.
    ''')

    user_choice = input('Whatcha wanna do? ')
    if user_choice == 'new':
        new_password()
    elif user_choice == 'show':
        pass
    else:
        print("Hwat?? That didn't compute") 