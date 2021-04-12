#register
# - first name, last name, password, email
# - generate user acount

#login
# - account number, password

#bank operations

#initializing the system
import random

database = {} #dictionary


def init():
   
    isValidOptionSelected = False
    print('Welcome to bankPHP')

    while isValidOptionSelected == False:

   
        haveAccount = int(input('Do you have an account with us: 1 (yes) 2 (no): \n'))
    
        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            print(register())
        else:
            print('You have selected an invalid option')

def login():

    print('Login to your account')

    bankOperation()

def register():

    print("***** Register *****")

    email = input('What is your email address? \n')
    first_name =  input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Create a password for yourself \n')

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print('Your account has been created')

    login()

def bankOperation():
    print('some operations')

def generationAccountNumber():

    
    return random.randrange(1111111111, 9999999999)
    




### Actual Banking System ###

init()



