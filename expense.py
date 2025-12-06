import sqlite3

# ------ DATABASE SETUP ------
def create_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            major TEXT
        )
    """)
    conn.commit()
    conn.close()


# ------ CRUD FUNCTIONS ------
def add_student(name, age, major):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
                   (name, age, major))
    conn.commit()
    conn.close()
    print("Student added successfully!")


def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_student(student_id, name, age, major):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students 
        SET name=?, age=?, major=?
        WHERE id=?
    """, (name, age, major, student_id))
    conn.commit()
    conn.close()
    print("Student updated successfully!")


def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted successfully!")


# ------ SIMPLE MENU ------
def menu():
    create_table()
    
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            major = input("Enter major: ")
            add_student(name, age, major)

        elif choice == "2":
            students = view_students()
            for s in students:
                print(s)

        elif choice == "3":
            sid = int(input("Enter student ID to update: "))
            name = input("New name: ")
            age = int(input("New age: "))
            major = input("New major: ")
            update_student(sid, name, age, major)

        elif choice == "4":
            sid = int(input("Enter student ID to delete: "))
            delete_student(sid)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again!")


# Run Program
menu()
