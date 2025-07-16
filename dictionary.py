student_marks = {'Alice':85, 'pooja':96, 'lucky':79,'anu':55}
name = input("enter the student's name: ")
if name in student_marks:
    print(f"{name}'s marks: ",student_marks[name])
else:
    print('student not found') 