#register
# - first name, last name, password, email
# - generate user acount

#login
# - account number, password

#bank operations

#initializing the system
import datetime
now = datetime.datetime.now()

import random

import validation

import database

from getpass import getpass

def init():
   
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    print('Welcome to bankPHP')

    
    haveAccount = int(input('Do you have an account with us: 1 (Yes) 2 (No): \n'))
    
    if(haveAccount == 1):
            
            login()
    elif(haveAccount == 2):
            
            register()
    else:
            print('Invalid Option Selected')

            int()

def login():

    print('+++++ Login +++++')

    accountNumberFromUser = input('What is your account number? \n')

    is_valid_account_number = validation.account_number_validation(accountNumberFromUser)
    
    if is_valid_account_number:

        password = getpass('What is your password? \n')
        
        user = database.authenticated_user(accountNumberFromUser, password)
       
        if user: 
           bankOperation(user)
       
       
                
        print('Invalid Login')
        login()

    else:
        print('Account Number Invalid, make sure you have 10 digits and only integers')
        init()
    



def register():

    print('+++++ Register +++++')

    email = input('What is your email address? \n')
    first_name =  input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = getpass('Create a password for yourself \n')
    
    accountNumber = generationAccountNumber()

    is_user_created = database.create(accountNumber, first_name, last_name, email, password)

    if is_user_created:

        print('Your account has been created')
        print('*************')
        print('Your account number is: %d' % accountNumber)
        print('Please keep it safe')        
        print('*************')

        login()

    else:
        print('Something went wrong, please try again')

        register()

def bankOperation(user):

    print('Welcome %s %s !' % ( user[0], user[1]))

   
    selectedOption = int(input('What would you like to do? (1) Deposit (2) Withdrawl (3) Logout (4) Exit (5) File a complaint \n'))

    if(selectedOption == 1):
        
        depositOperation()
    elif(selectedOption == 2):
        
        withdrawalOperation()
    elif(selectedOption == 3):
        
        logout()
    elif(selectedOption == 4):
        
        exit()
    elif(selectedOption == 5):
        
        complaintOperation()

    else:
        print('Invalid Option Selected')
    
    bankOperation(user)

def withdrawalOperation():
    print('You selected WITHDRAWAL')
    
    withdraw = input('How much would you like to withdraw? \n')
    
    print('Please take your cash')

    selectedOptions = int(input('Does that complete your transaction? (1) Yes (2) No \n'))

    if(selectedOptions == 1):
        
        init()

    elif(selectedOptions == 2):
        login()

    else:
        print('Invalid Option Selected')


def depositOperation():
    
    print('You selected DEPOSIT')
    
    deposit = input('How much would you like to deposit? \n')
    print('Your balance is %s' % deposit)
    
    selectedOptions = int(input('Does that complete your transaction? (1) Yes (2) No \n'))

    if(selectedOptions == 1):
        
        init()

    elif(selectedOptions == 2):
        login()

    else:
        print('Invalid Option Selected')

def complaintOperation():
    print('You selected COMPLAINT')
    
    complaint = input('Please briefly discuss your banking issue \n')

    print('We have received your complaint and will respond shortly - Thank you and have a great day')

    selectedOptions = int(input('Does that complete your transaction? (1) Yes (2) No \n'))

    if(selectedOptions == 1):
        
        init()

    elif(selectedOptions == 2):
        login()

    else:
        print('Invalid Option Selected')




def generationAccountNumber():

    
    return random.randrange(1111111111, 9999999999)

def get_current_balance(usersDetails):
    return userDetails[4] 

def logout():
    login()
    




### Actual Banking System ###
init()




