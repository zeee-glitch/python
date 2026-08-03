  #contact_book.py

# list to store contacts
contacts = []
#function to add a contact
def add_contact () :
    name = input("enter name: ")
    phone = input("enter phone number: ")
    email = input(" enteremail: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append (contact)
    print ("contact added successfully!")

    #function to search for a contact
    def search_contact(name):
      for contact in contacts:
          if contact["name"].lower() == name.lower():
              return contact
          return None

      #fuction to delete a contact
    def delete_contact (name):
      for  contact in contacts :
        if contact["name"].lower() ==name.lower():
           contacts . remove (contact)
           print("contact delete successfully!")

        return 
    
        print("contact not found.")

#fuction to view all contacts
        def view_all ():
                if len (contacts) == 0:
                    print ("no contacts available.")
                else:
                    print ("\n-----contact list-----")
                    for contact in contacts :
                        print (f"name : {contact ['name']}")
                        print (f"phone :{contact ['phone']}")
                        print (f"email :{contact ['email']}")
                        print ("-"* 25)
#main menu
                        while True :
                            print ("\n===== contact book=====")
                            print ("1. add contact")
                            print ("2. search contact")
                            print ("3. delect contact")
                            print ("4. view a;; contacts")
                            print ("5. exit")

                            choice = input ("enter your choice :")

                            if choice == "1":
                                add_contact ()

                            elif choice == "2":
                                name = input ("enter name to search:")
                                result = search_contsct(name)
                                if result:
                                    print ("\ncontact found:")
                                    print (f"name : {result ['name']}")
                                    print (f"phone : {result ['phone']}")
                                    print (f"email: {result ['email']}")
                                else:
                                    print ("contact not found.")
                            elif choice == "3":
                                name = input ("enter name to delete : ")
                                delete_contact (name)

                            elif  choice == "4":
                                view_all ()

                            elif choice == "5":
                                print ("thank you for using my contact book!")
                                break
                            else:
                                print ("invalid choice. please try again.")
                                


                                         