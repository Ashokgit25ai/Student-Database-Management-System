import json


FILENAME = "students.json"

def load_students():
    try:
        with open(FILENAME,'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def add_student(students):
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")
    
    students.append({
        "id" : sid,
        "name" : name,
        "age" : age,
        "course" : course,
        "marks" : marks
    })
    
    save_student(students)
    print("Student Added Successfully")
    
def save_student(students):
    with open(FILENAME,'w') as f:
        json.dump(students,f,indent=4)

def display_student(students):
    if not students:
        print("No Students Records found!")
        return

    print('\n----- STUDENT RECORDS ----')

    for s in students:
        print(
            f"ID: {s.get('id')} Name: {s.get('name')} Age: {s.get('age')} "
            f"Course: {s.get('course')} Marks: {s.get('marks')}"
        )
    
def search_student(students):
    sid = input("Enter the Student ID: ")
    
    for s in students:
         if s['id'] == sid:
            print(f'Found -> {s}')
            return
    print("Student Not Found in Records")
       
def update_student(students):
    
    sid = input("Enter the Student ID: ")
    
    for s in students:
        if s['id'] == sid:
            s['name'] = input("Enter Name: ")
            s['age'] = input("Enter Age: ")
            s['course'] = input("Enter Course: ")
            s['marks'] = input("Enter Marks: ")
            
            print("Update Student Record Successfully")
            return
        
        print("Student Record Not Found!")
        
    
def delete_student(students):
    sid = input("Enter the Student ID: ")
    
    for s in students:
         if s['id'] == sid:
            students.remove(s)
            print("Student Record Deleted Successfully")
            return
    print("Student Not Found in Records")
    
def main():
    
    students = load_students()
     
    while True:
        print("===== StudentDB Menu =====")
        print("1. Add Student")
        print("2. Display Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save & Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_student(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            save_student(students)
            print("Data saved. Exiting Program")
            break
        else:
            print("Invalid choice! Try again.")
            
if __name__ == "__main__":
    main()

