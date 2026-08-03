# student info formatter

# input

student_name = input("enter student name:")
student_number= input("enter student number:")
course = input("enter course:")
average_mark= float(input("enter average mark:"))

#output
print("n/-----student information-----")
print(f"Name      :{student_name}")
print(f"student no:{student_number}")
print(f"course    :{course}")
print(f"average mark :{average_mark:2f}%")

#checking pass or fail
if average_mark>50:
    print("status      :PASS")

else:
    print('status    :FAIL')
