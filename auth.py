#register
# - username, password, email
# - generate user acount

#login
# - (username or email) and password

#bank operations

#initializing the system

database = {}


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
            register()
        else:
            print('You have selected an invalid option')

def login():
    print('This is the login function')

def register():
    print('This is the register function')

def bankOperation():
    print('some operations')

def generationAccountNumber():
    print('account number generator')




### Actual Banking System ###

init()


