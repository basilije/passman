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


def find_password():
    looked_for_website = input('What website is it for? ')
    anything_found = False
    for entry in password_list:
        if looked_for_website == entry['website']:
            print('Found:')
            print('Username is:' + entry['username'])
            print('Password is:' + entry['password'])
            anything_found = True
    
    if not(anything_found):
        print("Not found!")

    #print(list(mydict.keys())[list(mydict.values()).index(value)]) # Prints george
    #looked_for_website = input('What website is it for? ')
    #print(search(password_list, looked_for_website))
    # for entry in password_list:
    #     found_website = entry.get('website')
    #     if found_website == looked_for_website:
    #         print(found_website)


while True:
    print('''
    Welcome to the password manager ya dingus.
    Type "new" to create a new password.
    Type "show" to look up a password.
    Type "find" to look up a username/password for the specific website.
    ''')

    user_choice = input('Whatcha wanna do? ')
    if user_choice == 'new':
        new_password()
    elif user_choice == 'show':
        pass
    elif user_choice == 'find':
        find_password()
    else:
        print("Hwat?? That didn't compute") 