# Student-Management-System
        
def add_students():
    students = []

    for i in range(5):
        name = input("Enter student name: ")
        marks = input("Enter student marks: ")

        students.append([name, marks])

    return students

def display_students(students):
    print("Student Records:")
    for student in students:
        print("Name:", student[0],"  " "---" "  " "Marks:", student[1])

# Main Program
student_list = add_students()
display_students(student_list)

