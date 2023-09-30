def create_student():
    students = {}
    students['class'] = input("Nhập lớp: ")
    students['name'] = input("Nhập tên: ")
    students['age'] = int(input("Nhập tuổi: "))
    students['grade'] = int(input("Nhập điểm: "))
    return students

def std_in_class():
    class_list = []
    class_name = input("Lớp: ")
    for student in students:
        if student['class'] == class_name:
            class_list.append(student['name'])
    class_lst = ', '.join(class_list)
    print(f"Lớp {class_name} gồm các học sinh:", class_lst)

def max_grade():
    max_grade = 0
    max_grade_student = None
    
    for student in students:
        if student['grade'] > max_grade:
            max_grade = student['grade']
            max_grade_student = student
    print(max_grade_student['name'])

students = []

n = int(input("Nhập số lượng học sinh trong lớp: "))
for i in range(n):
    student = create_student()
    students.append(student)

# print(students)
std_in_class()
max_grade()