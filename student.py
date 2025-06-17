# student.py

class Student:
    def __init__(self, name, roll_number, student_class, subjects=None, marks=None, gender=None, age=None, contact=None, parent_name=None, parent_contact=None, attendance=None, remarks=None, fee_status=None, photo_path=None, birthday=None):
        self.name = name
        self.roll_number = roll_number
        self.student_class = student_class
        self.subjects = subjects if subjects else []
        self.marks = marks if marks else {}
        self.gender = gender
        self.age = age
        self.contact = contact
        self.parent_name = parent_name
        self.parent_contact = parent_contact
        self.attendance = attendance if attendance else {}
        self.remarks = remarks
        self.fee_status = fee_status  # 'Paid' or 'Unpaid'
        self.photo_path = photo_path
        self.birthday = birthday

    def total_marks(self):
        return sum(self.marks.values())

    def percentage(self):
        if not self.marks or len(self.marks) == 0:
            return 0
        return self.total_marks() / len(self.marks)

    def grade(self, grading_scale=None):
        pct = self.percentage()
        scale = grading_scale or {
            90: 'A+', 80: 'A', 70: 'B', 60: 'C', 50: 'D', 0: 'F'
        }
        for boundary in sorted(scale.keys(), reverse=True):
            if pct >= boundary:
                return scale[boundary]
        return 'F'

    def is_pass(self, grading_scale=None):
        return self.grade(grading_scale) != 'F'

    def to_dict(self):
        return {
            'name': self.name,
            'roll_number': self.roll_number,
            'student_class': self.student_class,
            'subjects': self.subjects,
            'marks': self.marks,
            'gender': self.gender,
            'age': self.age,
            'contact': self.contact,
            'parent_name': self.parent_name,
            'parent_contact': self.parent_contact,
            'attendance': self.attendance,
            'remarks': self.remarks,
            'fee_status': self.fee_status,
            'photo_path': self.photo_path,
            'birthday': self.birthday
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data['name'],
            data['roll_number'],
            data['student_class'],
            data.get('subjects', []),
            data.get('marks', {}),
            data.get('gender'),
            data.get('age'),
            data.get('contact'),
            data.get('parent_name'),
            data.get('parent_contact'),
            data.get('attendance', {}),
            data.get('remarks'),
            data.get('fee_status'),
            data.get('photo_path'),
            data.get('birthday')
        )
