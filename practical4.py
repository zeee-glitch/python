#grade_classifier.py

#collect learner details
learner_name =input("enter leaner's name:")

subject1 = float(input("enter mark for subject1:"))
subject2 = float(input("enter mark for subject2:"))
subject3 = float(input("enter mark for subject3:"))

#calculate average
average =(subject1+ subject2 + subject3)/3
#assign letter grade
if average >=80:
    grade ="A"
elif average >=70:
    grade ="B"
elif average >=60:
    grade ="C"
elif average >=50:
    grade ="D"
else:
    grade ="F"

    #assign pass/fai status
    if average >= 50:
          status = "pass"
    else:
          status = "fail"

# Display report card
    print("\n=====STUDENT REPORT CARD=====")
    print(f"learner name: {learner_name}")
    print(f"subject 1   : {subject1}")
    print(f" subject 2  : {subject2}")
    print(f"subjec t3   :{subject3}")
    print(f"average    :{average:.2f}")
    print(f"grade      :{grade}")
    print(f"status     :{status}")

           #intervention flag
    print("\nIntervetion Report:")
    intervention = False

    if subject1 < 40:
           print("subject 1 need intervantion")
           intervention = True

           if subject2 < 40:
            print("subject 2 needs intervention")
    intervention = True

    if subject3 < 40:
           print ("subject 3 needs intervetion")
           intervention = True

           if not intervention:

            print ("No intervation required")
           



