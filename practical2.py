#secure password hint tool

#ask the user for their password

password= input("Enter your secret password:")
# remove accidental spaces
password = password.strip()
    #get the first and last letters
first_letter=password[0]
last_letter=password[-1]
#display the password hint
print(f"Your password hint:it starts with {first_letter.upper()}and ends with{last_letter.upper()}")

