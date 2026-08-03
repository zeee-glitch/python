#collect user information

first_name= input("Enter your first name:")
surname= input("Enter your  surname:")
age= int(input("Enter your age:"))
favourite_number= float(input("Eenter your favourite number:"))

#full name
full_name= first_name+ " "+ surname

#Greeting
print(f"/nwelcome, {full_name}!")

#string manipulation
print(f"Name in UPPERCASE :{full_name.upper()}")
print(f"Name in Title Case:{full_name.title()}")

#arithmetic
age_in_months= age*12
print(f"age in months   :{age_in_months}")

#round favourite number
rounded_number =round(favourite_number,2)
print(f"favourite number   :{rounded_number}")

#DATA TYPES
print("/ndata types")
print(f"first name     :{type(first_name)}")
print(f"surnsme        :{type(surname)}")
print(f"age            :{type(age)}")
print(f"favourite number:{type(favourite_number)}")



