# create record
# read record
# update record 
# delete record
# find user
# CRUD

def create(accountNumber, userDetails):

    f = open('data/user_record/' + str(accountNumber) + '.txt', 'x')
    f.write(str(userDetails));
    f.close();

    #create a file
    # name of the file would be account_number.txt
    # add user details to the file
    # return true
    # if saving to file fails, then delete created file)

def read(userAccountNumber):
    print('read user record')
    # find user with account numnber
    # fetch contents of the file

def update(userAccountNumber):
    print('update user record')
    # find user with account numnber
    # fetch the content of the file
    # update the content of the file
    # save the file 
    # return true

def delete(userAccountNumber):
    print('delete user record')
    # find user with account number
    # return true

def find(userAccountNumber):
    print('find user')
    # find user record in the data folder


create(9316394511, ['Cierra', 'Triche', 'mscasy9@yahoo.com', 'password', 250])