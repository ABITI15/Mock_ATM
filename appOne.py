import datetime
now = datetime.datetime.now()


name = input('What is your name? \n')
allowedUsers = ['Cassie', 'CiCi', 'Rene']
allowedPassword = ['PasswordC', 'PasswordR', 'PasswordT']

if(name in allowedUsers):
    password = input('Your password? \n')
    userID = allowedUsers.index(name)
   
    if(password == allowedPassword[userID]):
        print(now.strftime('%Y-%m-%d %H:%M:%S'))
        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:' ))

        if(selectedOption == 1):
            print('You selected %s' % selectedOption)
           
            withdraw = input('How much would you like to withdraw? \n')
            print('Please take your cash')

            print(now.strftime('%Y-%m-%d %H:%M:%S'))
            print('Welcome %s' % name)
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Complaint')

            selectedOption = int(input('Please select an option:' ))

        elif(selectedOption == 2):
            print('You selected %s' % selectedOption)

            deposit = input('How much would you like to deposit? \n')
            print('Your balance is %s' % deposit)

            print(now.strftime('%Y-%m-%d %H:%M:%S'))
            print('Welcome %s' % name)
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Complaint')

            selectedOption = int(input('Please select an option:' ))

        elif(selectedOption == 3):
            print('You selected %s' % selectedOption)

            complaint = input('What issue would you like to report? \n')
            print('Thank you for contacting us')
            print(now.strftime('%Y-%m-%d %H:%M:%S'))
            print('Welcome %s' % name)
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Complaint')
       
            selectedOption = int(input('Please select an option:' ))
            
        else:
            print('Invalid option selected, please try again')
            
    else:
        print('Password Incorrect, please try again') 
else:
    print('Name not found, please try again')
