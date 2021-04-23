def account_number_validation(accountNumber):
    # check if accountNumber is not empty
    # if accountNumber is 10 digits
    # if the accountNumber is an integer
    if accountNumber:

        if len(str(accountNumber)) == 10:

            try: 
                int(accountNumber)
                return True
            
            except ValueError:
                print('Invalid Account number, account number should be an integer')
                return False

            except TypeError:
                print('Invalid account type')
                return False
        
        else:
            print('Account number cannot be more than 10 digits')
            return False
    else:   
        print('Account number is a required field')
        return False