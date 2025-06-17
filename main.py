# main.py
import os
import json
from student import Student
from colorama import init, Fore, Style
init(autoreset=True)

ADMIN_USER = 'mujtaba'
ADMIN_PASS = 'admin'

DATA_FILE = 'data.txt'
BACKUP_FILE = 'data_backup.txt'

# Helper functions for file handling
def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            data = json.load(f)
            return [Student.from_dict(s) for s in data]
        except Exception:
            return []

def save_students(students):
    with open(DATA_FILE, 'w') as f:
        json.dump([s.to_dict() for s in students], f, indent=2)

def find_student(students, roll_number):
    for s in students:
        if s.roll_number == roll_number:
            return s
    return None

def admin_login():
    print(Fore.CYAN + "\n==== Admin Login ====")
    for _ in range(3):
        user = input("Username: ")
        pwd = input("Password: ")
        if user == ADMIN_USER and pwd == ADMIN_PASS:
            print(Fore.GREEN + "Login successful!")
            return True
        else:
            print(Fore.RED + "Invalid credentials.")
    print(Fore.RED + "Too many failed attempts. Exiting.")
    exit()

def main_menu():
    while True:
        print("\n==============================")
        print(Fore.YELLOW + " Welcome to Student Result App")
        print("==============================")
        print("1. Add Student")
        print("2. Enter Marks")
        print("3. View Result")
        print("4. Search Student")
        print("5. Update Info")
        print("6. Delete Student")
        print("7. Show All Students")
        print("8. Topper List / Subject Wise Topper")
        print("9. Export Result")
        print("10. Backup Data")
        print("11. Restore Data")
        print("12. Class/Subject Statistics")
        print("13. Birthday Reminders")
        print("14. Search by Contact/Age")
        print("15. Paginate Student List")
        print("16. Promote Students")
        print("17. Mark Attendance")
        print("18. View Attendance")
        print("19. Generate ID Card")
        print("20. Send SMS Notification (Stub)")
        print("21. Parent Portal Access")
        print("22. Transfer/Withdraw Student")
        print("23. Alumni Management")
        print("24. Document Tracking")
        print("25. Custom Reports")
        print("26. Timetable Management (Stub)")
        print("27. Health Record Tracking")
        print("28. Search Filters")
        print("29. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            enter_marks()
        elif choice == '3':
            view_result()
        elif choice == '4':
            search_student()
        elif choice == '5':
            update_student()
        elif choice == '6':
            delete_student()
        elif choice == '7':
            show_all_students()
        elif choice == '8':
            show_toppers()
        elif choice == '9':
            export_result()
        elif choice == '10':
            backup_data()
        elif choice == '11':
            restore_data()
        elif choice == '12':
            class_statistics()
        elif choice == '13':
            birthday_reminders()
        elif choice == '14':
            search_by_contact_or_age()
        elif choice == '15':
            paginate_students()
        elif choice == '16':
            promote_students()
        elif choice == '17':
            mark_attendance()
        elif choice == '18':
            view_attendance()
        elif choice == '19':
            generate_id_card()
        elif choice == '20':
            send_sms_notification()
        elif choice == '21':
            parent_portal()
        elif choice == '22':
            transfer_withdraw_student()
        elif choice == '23':
            alumni_management()
        elif choice == '24':
            document_tracking()
        elif choice == '25':
            custom_reports()
        elif choice == '26':
            timetable_management()
        elif choice == '27':
            health_record_tracking()
        elif choice == '28':
            search_filters()
        elif choice == '29':
            print(Fore.CYAN + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid option. Try again.")

def add_student():
    students = load_students()
    name = input("Enter Name: ")
    roll_number = input("Enter Roll Number (unique): ")
    if any(s.roll_number == roll_number for s in students):
        print("Roll Number already exists!")
        return
    student_class = input("Enter Class: ")
    subjects = input("Enter Subjects (comma separated): ").split(',')
    gender = input("Enter Gender (optional): ")
    age = input("Enter Age (optional): ")
    contact = input("Enter Contact (optional): ")
    parent_name = input("Enter Parent/Guardian Name (optional): ")
    parent_contact = input("Enter Parent/Guardian Contact (optional): ")
    fee_status = input("Fee Status (Paid/Unpaid): ") or 'Unpaid'
    photo_path = input("Photo Path (optional): ")
    birthday = input("Birthday (DD-MM, optional): ")
    student = Student(name, roll_number, student_class, [s.strip() for s in subjects], gender=gender or None, age=age or None, contact=contact or None, parent_name=parent_name or None, parent_contact=parent_contact or None, fee_status=fee_status, photo_path=photo_path or None, birthday=birthday or None)
    students.append(student)
    save_students(students)
    print("Student added successfully.")

def enter_marks():
    students = load_students()
    roll_number = input("Enter Roll Number: ")
    student = find_student(students, roll_number)
    if not student:
        print("Student not found.")
        return
    for subject in student.subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        student.marks[subject] = mark
    save_students(students)
    print("Marks updated.")

def view_result():
    students = load_students()
    roll_number = input("Enter Roll Number: ")
    student = find_student(students, roll_number)
    if not student:
        print("Student not found.")
        return
    print("\n======= Student Result =======")
    print(f"Name      : {student.name}")
    print(f"Roll No   : {student.roll_number}")
    print(f"Class     : {student.student_class}")
    print(f"Gender    : {student.gender}")
    print(f"Age       : {student.age}")
    print(f"Contact   : {student.contact}")
    print(f"Subjects  : {', '.join(student.subjects)}")
    print("Marks:")
    for sub, mark in student.marks.items():
        print(f"  {sub}: {mark}")
    print(f"Total     : {student.total_marks()}")
    print(f"Percentage: {student.percentage():.2f}")
    print(f"Grade     : {student.grade()}")
    print(f"Status    : {'Pass' if student.is_pass() else 'Fail'}")
    print("==============================")

def update_student():
    students = load_students()
    roll_number = input("Enter Roll Number: ")
    student = find_student(students, roll_number)
    if not student:
        print("Student not found.")
        return
    name = input(f"Enter Name [{student.name}]: ") or student.name
    student_class = input(f"Enter Class [{student.student_class}]: ") or student.student_class
    subjects = input(f"Enter Subjects (comma separated) [{', '.join(student.subjects)}]: ")
    if subjects:
        student.subjects = [s.strip() for s in subjects.split(',')]
    gender = input(f"Enter Gender [{student.gender}]: ") or student.gender
    age = input(f"Enter Age [{student.age}]: ") or student.age
    contact = input(f"Enter Contact [{student.contact}]: ") or student.contact
    parent_name = input(f"Enter Parent/Guardian Name [{student.parent_name}]: ") or student.parent_name
    parent_contact = input(f"Enter Parent/Guardian Contact [{student.parent_contact}]: ") or student.parent_contact
    fee_status = input(f"Fee Status (Paid/Unpaid) [{student.fee_status}]: ") or student.fee_status
    photo_path = input(f"Photo Path [{student.photo_path}]: ") or student.photo_path
    birthday = input(f"Birthday (DD-MM) [{student.birthday}]: ") or student.birthday
    remarks = input(f"Remarks [{student.remarks}]: ") or student.remarks
    student.name = name
    student.student_class = student_class
    student.gender = gender
    student.age = age
    student.contact = contact
    student.parent_name = parent_name
    student.parent_contact = parent_contact
    student.fee_status = fee_status
    student.photo_path = photo_path
    student.birthday = birthday
    student.remarks = remarks
    save_students(students)
    print("Student info updated.")

def delete_student():
    students = load_students()
    roll_number = input("Enter Roll Number: ")
    student = find_student(students, roll_number)
    if not student:
        print("Student not found.")
        return
    confirm = input(f"Are you sure you want to delete {student.name} (Roll: {student.roll_number})? (y/n): ")
    if confirm.lower() != 'y':
        print("Delete cancelled.")
        return
    new_students = [s for s in students if s.roll_number != roll_number]
    save_students(new_students)
    print("Student deleted.")

def show_all_students():
    students = load_students()
    if not students:
        print("No students found.")
        return
    students.sort(key=lambda s: (s.name.lower(), s.roll_number))
    print("\n{:<15} {:<10} {:<8} {:<10} {:<10}".format('Name', 'Roll No', 'Class', 'Percent', 'Grade'))
    print("-"*60)
    for s in students:
        print("{:<15} {:<10} {:<8} {:<10.2f} {:<10}".format(s.name, s.roll_number, s.student_class, s.percentage(), s.grade()))

def show_toppers():
    students = load_students()
    if not students:
        print("No students found.")
        return
    # Top 3 by percentage
    toppers = sorted(students, key=lambda s: s.percentage(), reverse=True)[:3]
    print("\nTop 3 Students:")
    for idx, s in enumerate(toppers, 1):
        print(f"{idx}. {s.name} (Roll: {s.roll_number}) - {s.percentage():.2f}%")
    # Subject-wise toppers
    all_subjects = set(sub for s in students for sub in s.subjects)
    print("\nSubject-wise Toppers:")
    for subject in all_subjects:
        top = max(students, key=lambda s: s.marks.get(subject, 0))
        print(f"{subject}: {top.name} (Roll: {top.roll_number}) - {top.marks.get(subject, 0)}")

def export_result():
    students = load_students()
    roll_number = input("Enter Roll Number to export result: ")
    student = find_student(students, roll_number)
    if not student:
        print(Fore.RED + "Student not found.")
        return
    filename = f"result_{student.roll_number}.txt"
    with open(filename, 'w') as f:
        f.write(f"===== Student Result =====\n")
        f.write(f"Name      : {student.name}\n")
        f.write(f"Roll No   : {student.roll_number}\n")
        f.write(f"Class     : {student.student_class}\n")
        f.write(f"Gender    : {student.gender}\n")
        f.write(f"Age       : {student.age}\n")
        f.write(f"Contact   : {student.contact}\n")
        f.write(f"Subjects  : {', '.join(student.subjects)}\n")
        f.write("Marks:\n")
        for sub, mark in student.marks.items():
            f.write(f"  {sub}: {mark}\n")
        f.write(f"Total     : {student.total_marks()}\n")
        f.write(f"Percentage: {student.percentage():.2f}\n")
        f.write(f"Grade     : {student.grade()}\n")
        f.write(f"Status    : {'Pass' if student.is_pass() else 'Fail'}\n")
        f.write("==========================\n")
    print(Fore.GREEN + f"Result exported to {filename}")

def backup_data():
    import shutil
    shutil.copy(DATA_FILE, BACKUP_FILE)
    print(Fore.GREEN + f"Backup created as {BACKUP_FILE}")

def restore_data():
    import shutil
    if not os.path.exists(BACKUP_FILE):
        print(Fore.RED + "No backup found.")
        return
    shutil.copy(BACKUP_FILE, DATA_FILE)
    print(Fore.GREEN + "Data restored from backup.")

def class_statistics():
    students = load_students()
    if not students:
        print(Fore.YELLOW + "No students found.")
        return
    class_dict = {}
    for s in students:
        class_dict.setdefault(s.student_class, []).append(s)
    for cls, studs in class_dict.items():
        print(Fore.CYAN + f"\nClass: {cls}")
        for subject in set(sub for s in studs for sub in s.subjects):
            marks = [s.marks.get(subject, 0) for s in studs if subject in s.marks]
            if marks:
                print(f"  {subject}: Avg={sum(marks)/len(marks):.2f}, High={max(marks)}, Low={min(marks)}")

def birthday_reminders():
    students = load_students()
    today = input("Enter today's date (DD-MM): ")
    found = False
    for s in students:
        if hasattr(s, 'birthday') and s.birthday == today:
            print(Fore.MAGENTA + f"Birthday: {s.name} (Roll: {s.roll_number})")
            found = True
    if not found:
        print(Fore.YELLOW + "No birthdays today.")

def search_by_contact_or_age():
    students = load_students()
    query = input("Enter Contact or Age to search: ").strip()
    found = False
    for s in students:
        if (s.contact and query in str(s.contact)) or (s.age and query == str(s.age)):
            print(f"Name: {s.name}, Roll: {s.roll_number}, Contact: {s.contact}, Age: {s.age}")
            found = True
    if not found:
        print(Fore.YELLOW + "No student found.")

def paginate_students():
    students = load_students()
    if not students:
        print(Fore.YELLOW + "No students found.")
        return
    per_page = 5
    total = len(students)
    page = 0
    while True:
        start = page * per_page
        end = start + per_page
        print(Fore.CYAN + f"\nShowing students {start+1}-{min(end, total)} of {total}")
        for s in students[start:end]:
            print(f"{s.name} (Roll: {s.roll_number})")
        if end >= total:
            break
        next_page = input("Show next page? (y/n): ")
        if next_page.lower() != 'y':
            break
        page += 1

def promote_students():
    students = load_students()
    promoted = 0
    for s in students:
        if s.is_pass():
            try:
                s.student_class = str(int(s.student_class) + 1)
                promoted += 1
            except:
                continue
    save_students(students)
    print(Fore.GREEN + f"{promoted} students promoted to next class.")

def mark_attendance():
    students = load_students()
    date = input("Enter date for attendance (DD-MM-YYYY): ")
    for s in students:
        status = input(f"Is {s.name} (Roll: {s.roll_number}) present? (y/n): ")
        s.attendance[date] = 'Present' if status.lower() == 'y' else 'Absent'
    save_students(students)
    print("Attendance marked for all students.")

def view_attendance():
    students = load_students()
    roll_number = input("Enter Roll Number: ")
    student = find_student(students, roll_number)
    if not student:
        print("Student not found.")
        return
    print(f"Attendance for {student.name} (Roll: {student.roll_number}):")
    for date, status in student.attendance.items():
        print(f"  {date}: {status}")

def search_student():
    students = load_students()
    query = input("Enter Name or Roll Number to search: ").lower()
    found = False
    for s in students:
        if query in s.name.lower() or query == s.roll_number.lower():
            print(f"\nName: {s.name}\nRoll: {s.roll_number}\nClass: {s.student_class}\nGender: {s.gender}\nAge: {s.age}\nContact: {s.contact}\nSubjects: {', '.join(s.subjects)}\nMarks: {s.marks}\nTotal: {s.total_marks()}\nPercentage: {s.percentage():.2f}\nGrade: {s.grade()}\nStatus: {'Pass' if s.is_pass() else 'Fail'}")
            found = True
    if not found:
        print("No student found.")

def generate_id_card():
    students = load_students()
    roll_number = input("Enter Roll Number for ID card: ")
    student = find_student(students, roll_number)
    if not student:
        print(Fore.RED + "Student not found.")
        return
    filename = f"ID_{student.roll_number}.txt"
    with open(filename, 'w') as f:
        f.write(f"===== Student ID Card =====\n")
        f.write(f"Name      : {student.name}\n")
        f.write(f"Roll No   : {student.roll_number}\n")
        f.write(f"Class     : {student.student_class}\n")
        f.write(f"Gender    : {student.gender}\n")
        f.write(f"Age       : {student.age}\n")
        f.write(f"Contact   : {student.contact}\n")
        f.write(f"Parent    : {student.parent_name}\n")
        f.write(f"Parent Contact: {student.parent_contact}\n")
        f.write(f"Photo Path: {student.photo_path}\n")
        f.write(f"==========================\n")
    print(Fore.GREEN + f"ID card exported to {filename}")

def send_sms_notification():
    print(Fore.YELLOW + "(Stub) SMS notification feature requires SMS API integration.")

def parent_portal():
    students = load_students()
    roll_number = input("Enter your child's Roll Number: ")
    student = find_student(students, roll_number)
    if not student:
        print(Fore.RED + "Student not found.")
        return
    print(f"\nName: {student.name}\nClass: {student.student_class}\nAttendance: {len([v for v in student.attendance.values() if v == 'Present'])} days present\nFee Status: {student.fee_status}\nRemarks: {student.remarks}")

def transfer_withdraw_student():
    students = load_students()
    roll_number = input("Enter Roll Number: ")
    student = find_student(students, roll_number)
    if not student:
        print(Fore.RED + "Student not found.")
        return
    status = input("Mark as (Transferred/Withdrawn): ")
    reason = input("Reason: ")
    date = input("Date (DD-MM-YYYY): ")
    student.remarks = f"{status} on {date}: {reason}"
    save_students(students)
    print(Fore.GREEN + f"Student marked as {status}.")

def alumni_management():
    students = load_students()
    print("Alumni (Graduated Students):")
    for s in students:
        if s.student_class.lower() in ['alumni', 'graduated']:
            print(f"{s.name} (Roll: {s.roll_number})")

def document_tracking():
    students = load_students()
    roll_number = input("Enter Roll Number: ")
    student = find_student(students, roll_number)
    if not student:
        print(Fore.RED + "Student not found.")
        return
    docs = input("Enter submitted documents (comma separated): ")
    student.remarks = (student.remarks or "") + f" | Docs: {docs}"
    save_students(students)
    print(Fore.GREEN + "Documents updated.")

def custom_reports():
    students = load_students()
    print("1. Students failing in 2+ subjects")
    print("2. Fee defaulters")
    choice = input("Choose report: ")
    if choice == '1':
        for s in students:
            fails = sum(1 for m in s.marks.values() if m < 33)
            if fails >= 2:
                print(f"{s.name} (Roll: {s.roll_number}) - Failing in {fails} subjects")
    elif choice == '2':
        for s in students:
            if s.fee_status and s.fee_status.lower() == 'unpaid':
                print(f"{s.name} (Roll: {s.roll_number}) - Fee Unpaid")

def timetable_management():
    print(Fore.YELLOW + "(Stub) Timetable management feature can be added with a timetable field per class.")

def health_record_tracking():
    students = load_students()
    roll_number = input("Enter Roll Number: ")
    student = find_student(students, roll_number)
    if not student:
        print(Fore.RED + "Student not found.")
        return
    blood_group = input("Enter Blood Group: ")
    allergies = input("Enter Allergies (comma separated): ")
    student.remarks = (student.remarks or "") + f" | Blood Group: {blood_group}, Allergies: {allergies}"
    save_students(students)
    print(Fore.GREEN + "Health info updated.")

def search_filters():
    students = load_students()
    print("Filter by: 1. Class 2. Gender 3. Fee Status")
    choice = input("Choose filter: ")
    if choice == '1':
        cls = input("Enter class: ")
        for s in students:
            if s.student_class == cls:
                print(f"{s.name} (Roll: {s.roll_number})")
    elif choice == '2':
        gender = input("Enter gender: ")
        for s in students:
            if s.gender and s.gender.lower() == gender.lower():
                print(f"{s.name} (Roll: {s.roll_number})")
    elif choice == '3':
        status = input("Enter fee status (Paid/Unpaid): ")
        for s in students:
            if s.fee_status and s.fee_status.lower() == status.lower():
                print(f"{s.name} (Roll: {s.roll_number})")

if __name__ == "__main__":
    admin_login()
    main_menu()
