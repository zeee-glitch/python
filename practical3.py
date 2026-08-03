#username and message formatter
#collect user inp
first_name=input("enter your first name:")
last_name=input("enter your last name:")
bio=input("enter your bio:")
#createuser input
username= first_name[0].lower()+last_name.lower()
#format fuul  name
full_name=f"{first_name} {last_name}".title()
#clean up the bio
bio=bio.strip()
#count the characters in the bio
bio_length=len(bio)
# replace "i am"with "i'm"
bio=bio.replace("iam","i'm")
#display the formatted profilr
print(f"/nUsername :{username}")
print(f"Full Name  :{full_name}")
print(f"Bio        :{bio}")
print(f"Bio length :{bio_length}characters")




