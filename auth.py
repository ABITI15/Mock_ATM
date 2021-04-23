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

database = {
    9316394511: ['Cierra', 'Triche', 'mscasy9@yahoo.com', 'password', 250] 
} 
#dictionary


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
  
        password = input('What is your password? \n')

        for accountNumber, userDetails in database.items():
            if accountNumber == int(accountNumberFromUser):
                if(userDetails[3] == password):
                    bankOperation(userDetails)
                
        print('Invalid Login')
        login()

    else:
        init()
    



def register():

    print('+++++ Register +++++')

    email = input('What is your email address? \n')
    first_name =  input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Create a password for yourself \n')

    
    
    accountNumber = generationAccountNumber()
    

    database[accountNumber] = [first_name, last_name, email, password, 0]

    print('Your account has been created')
    print('*************')
    print('Your account number is: %d' % accountNumber)
    print('Please keep it safe')
    print('*************')

    login()

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




