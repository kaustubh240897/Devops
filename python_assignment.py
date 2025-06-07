# first program  Grade Checker


i = int(input("your score"))
if i > 90:
    print("A")
elif i> 80:
    print("B")
elif i> 70:
    print("C")
elif i>60:
    print("D")
else:
    print("F")

#---------------------------------------------
# second program 
# Student Grades


student_grades = {}

#Add a new student and grade.

def add_student():
    name = input("Add student name")
    if name in student_grades:
        print(f"{name} already exist with {student_grades[name]}.")
    else:
        grade = input(f"Enter grade for {name}: ")
        student_grades[name] = grade
        print(f"Added {name} grade with {grade}")

# Update an existing student’s grade.

def update_grade():
    name = input("Enter student name to update: ")
    if name in student_grades:
        grade = input(f"Enter new grade for {name}: ")
        student_grades[name] = grade
        print(f"Updated {name}'s grade to {grade}.")
    else:
        print(f"{name} not found in records.")

# Print all student grades.

def print_grades():
    if not student_grades:
        print("no student grade available")
    else:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")


# Menu-driven interface
while True:
    print("\n1. Add Student")
    print("2. Update Student Grade")
    print("3. Print All Grades")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        update_grade()
    elif choice == '3':
        print_grades()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")



#---------------------------------------------

# third program 
# Write to a File


file = open("simple.txt", "w")

file.write("Hiii this is my simple file \n")
file.write("I am write some random text")

file.close()

print("file is created.")



#---------------------------------------------

# fourth program 
# Read from a File

file = open("simple.txt", "r")
content = file.read()
print("file content is : \n",content)






