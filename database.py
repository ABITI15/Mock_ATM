# create record
# read record
# update record 
# delete record
# find user
# CRUD

import os
import validation

user_db_path = 'data/user_record/'

def create(userAccountNumber, first_name, last_name, email, password):
    
    user_data = first_name + '' + last_name + ',' + email + ',' + password + ',' + str(0)
    
    
    if does_account_number_exist(userAccountNumber):                    
        return False
    
    if does_email_exist(email):
        print('User already exists')
        return False

    completion_state = False

    
    try: 

        f = open(user_db_path  + str(userAccountNumber) + '.txt', 'x')

    except FileExistsError:
        
        
        does_file_contain_data = read(user_db_path  + str(userAccountNumber) + '.txt')
            
        if not does_file_contain_data:
            delete(userAccountNumber)    
        
        # delete the already created file, and print out error, then return false
        # check contents of file before deleting
        
    else:
        f.write(str(user_data));
        
        completion_state = True
        

    finally:
        f.close();

        return completion_state

    #create a file
    # name of the file would be account_number.txt
    # add user details to the file
    # return true
    # if saving to file fails, then delete created file)

def read(userAccountNumber):
   
    # find user with account numnber
    # fetch contents of the file

    is_valid_account_number = validation.account_number_validation(userAccountNumber)
    
    try:
        
        if is_valid_account_number:

            f = open(user_db_path + str(userAccountNumber) + '.txt', 'r')
    
        else:

            f = open(user_db_path + userAccountNumber, 'r')

    except FileNotFoundError:
        print('User not found')
    
    except FileExistsError:
        print('User does not exit')

    except TypeError:
        print('Invalid account number format')
    
    
    else:
        return f.readline()

    return False

def update(userAccountNumber):
    print('update user record')
    # find user with account numnber
    # fetch the content of the file
    # update the content of the file
    # save the file 
    # return true

def delete(userAccountNumber):

    is_delete_successful = False

    if os.path.exists(user_db_path + str(userAccountNumber) + '.txt'):
        

        try:  

            os.remove(user_db_path + str(userAccountNumber) + '.txt')
            is_delete_successful = True

        except FileNotFoundError:
            print('User not found')

        finally:

            return is_delete_successful
    
    # find user with account number
    # return true

def does_email_exist(email):
    
    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')

        if email in user_list:
            return True

    return False


def does_account_number_exist(userAccountNumber):

    all_users = os.listdir(user_db_path)

    for user in all_users:
        
        if user == str(userAccountNumber) + '.txt':

            return True

    return False


def authenticated_user(accountNumber, password):
    
    if does_account_number_exist(accountNumber):
    
        user = str.split(read(accountNumber), ',')
    
        if password == user[2]:
            return user
    
    return False
 
 # print(does_account_number_exist(9804907910))

# find user record in the data folder

# print(read({'One':'Two'}))