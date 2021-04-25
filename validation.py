def account_number_validation(accountNumber):
    # check if accountNumber is not empty
    # if accountNumber is 10 digits
    # if the accountNumber is an integer
    if accountNumber:

        try: 
            int(accountNumber)
                
            if len(str(accountNumber)) == 10:
                    
                return True
            
        except ValueError:
           
                return False

        except TypeError:
            
                return False
          
        
    return False