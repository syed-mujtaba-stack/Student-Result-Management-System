# Student Result Management System (CLI Based)

A comprehensive, feature-rich command-line application for managing student records, results, attendance, and more. Built with Python and OOP principles, this system is ideal for schools and educational institutions.

---

## 🚀 Features

- **Student Registration**: Name, Roll Number, Class, Subjects, Gender, Age, Contact, Parent/Guardian Info, Photo, Birthday, and more.
- **Marks Management**: Enter, update, and view subject-wise marks. Automatic calculation of total, percentage, grade, and pass/fail status.
- **Attendance Tracking**: Mark and view daily attendance for each student.
- **Parent Portal**: CLI access for parents to view their child's results and attendance.
- **Fee Management**: Track paid/unpaid status.
- **Remarks & Health Records**: Add teacher remarks, health info, and document tracking.
- **ID Card Generator**: Export printable student ID cards.
- **Export/Import**: Export results and ID cards as `.txt` files. Bulk import/export via CSV (extendable).
- **Custom Reports**: Generate reports for failing students, fee defaulters, and more.
- **Alumni Management**: Track graduated students.
- **Search & Filters**: Search by name, roll number, contact, age, class, gender, fee status, and more.
- **Class/Subject Statistics**: View averages, highs, and lows.
- **Promotion & Transfer**: Promote students or mark as transferred/withdrawn.
- **Backup/Restore**: Data safety with backup and restore options.
- **Multi-user Support**: (Extendable) Roles for admin, teacher, parent.
- **Colorful CLI**: Enhanced readability using `colorama`.

---

## 🖥️ Sample CLI Menu

```
==============================
 Welcome to Student Result App
==============================
1. Add Student
2. Enter Marks
3. View Result
4. Search Student
5. Update Info
6. Delete Student
7. Show All Students
8. Topper List / Subject Wise Topper
9. Export Result
10. Backup Data
11. Restore Data
12. Class/Subject Statistics
13. Birthday Reminders
14. Search by Contact/Age
15. Paginate Student List
16. Promote Students
17. Mark Attendance
18. View Attendance
19. Generate ID Card
20. Send SMS Notification (Stub)
21. Parent Portal Access
22. Transfer/Withdraw Student
23. Alumni Management
24. Document Tracking
25. Custom Reports
26. Timetable Management (Stub)
27. Health Record Tracking
28. Search Filters
29. Exit
```

---

## ⚙️ How to Run

1. **Install Python 3.7+**
2. **Install dependencies:**
   ```bash
   pip install colorama
   ```
3. **Run the app:**
   ```bash
   python main.py
   ```

---

## 📦 File Structure

- `main.py` — Main CLI application
- `student.py` — Student class and data model
- `data.txt` — Persistent data storage (JSON format)

---

## 📝 Customization & Extensions
- Add real SMS/email integration
- Implement a GUI or web interface
- Add more user roles and permissions
- Connect to a real database (SQLite, MySQL, etc.)

---

## 🙏 Credits
Developed by Syed Mujtaba Abbas.

---

## 📄 License
MIT License
#   S t u d e n t - R e s u l t - M a n a g e m e n t - S y s t e m  
 