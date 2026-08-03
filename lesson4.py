# basic if/else statement script
age= int(input("enter your age"))
section_pass= input("do you have a vip ticket?(yes/no)").lower()
if age>= 18 and section_pass=="yes":
         print("access gtanted to the VIP section!!!")
if age>= 18:
         print ("access granted to the general section!!!")
else:
          print("access denied!!!")
