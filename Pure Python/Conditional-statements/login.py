'''
Create an app that asks a user for their username and password and validates 
that they can log in to a fictional app.

If they are the same as the valid username and password, 
print a message welcoming the user by their username.

If either the username or the password is blank, 
print a message telling them they must enter a username and password.

The default case should be to tell the user that the username or password was incorrect
'''

valid_username = "monkify11235"
valid_password = "code"

username = input("Username: ")
password = input("Password: ")

if username == valid_password and password == valid_password:
    print("Access granted")
    
