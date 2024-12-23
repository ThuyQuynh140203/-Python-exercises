# doc danh sach sinh vien tu file
def read_students(file_name):
    students = []
    if not file_name:
        print("Tập tin không tồn tại.")
        return students
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            student_info = line.strip().split('|')
            students.append(student_info)
    return students

# hien thi danh sach sinh vien
def display_students(students):
    print(f"{'Mã SV':<10}{'Họ và chữ lót':<20}{'Tên':<15}{'Lớp':<10}{'Quê quán'}")
    for student in students:
        print(f"{student[0]:<10}{student[1] + ' ' + student[2]:<20}{student[3]:<15}{student[3]:<10}{student[4]}")

# nhap thong tin sinh vien
def add_student():
    student_id = input("Nhập mã số sinh viên: ")
    first_name = input("Nhập họ và chữ lót sinh viên: ")
    last_name = input("Nhập tên sinh viên: ")
    class_name = input("Nhập lớp sinh viên: ")
    hometown = input("Nhập quê quán: ")
    return [student_id, first_name, last_name, class_name, hometown]

# sua thong tin sinh vien
def edit_student(students, student_id):
    for student in students:
        if student[0] == student_id:
            print(f"Sửa thông tin sinh viên {student_id}:")
            student[1] = input("Nhập lại họ và chữ lót: ")
            student[2] = input("Nhập lại tên sinh viên: ")
            student[3] = input("Nhập lại lớp: ")
            student[4] = input("Nhập lại quê quán: ")
            print("Thông tin đã được sửa thành công.")
            return students
    print("Mã sinh viên không tồn tại.")
    return students

# luu danh sach sinh vien
def save_students(file_name, students):
    with open(file_name, 'w', encoding='utf-8') as file:
        for student in students:
            file.write('|'.join(student) + '\n')
    print("Danh sách sinh viên đã được lưu.")

# Hàm hien thi sinh vien theo lop
def display_by_class(students, class_name):
    print(f"\nDanh sách sinh viên lớp {class_name}:")
    class_students = [student for student in students if student[3] == class_name]
    display_students(class_students)

# Hien thi sinh vien theo ten
def display_by_name(students, name):
    print(f"\nDanh sách sinh viên tên {name}:")
    name_students = [student for student in students if student[2] == name]
    display_students(name_students)

# Hàm lưu sinh viên theo lớp vào file riêng
def save_students_by_class(students, class_name):
    class_students = [student for student in students if student[3] == class_name]
    file_name = f"Sinhvien_{class_name}.txt"
    save_students(file_name, class_students)

# Main function
def main():
    file_name = "Sinhvien.txt"
    students = read_students(file_name)

    while True:
        print("\nChương trình quản lý sinh viên")
        print("1. Hiển thị danh sách sinh viên")
        print("2. Nhập thông tin sinh viên mới")
        print("3. Sửa thông tin sinh viên")
        print("4. Lưu danh sách sinh viên vào file")
        print("5. Hiển thị danh sách sinh viên theo lớp")
        print("6. Hiển thị danh sách sinh viên theo tên")
        print("7. Lưu sinh viên theo lớp vào file riêng")
        print("8. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            display_students(students)
        elif choice == '2':
            students.append(add_student())
        elif choice == '3':
            student_id = input("Nhập mã số sinh viên cần sửa: ")
            students = edit_student(students, student_id)
        elif choice == '4':
            save_students(file_name, students)
        elif choice == '5':
            class_name = input("Nhập lớp sinh viên cần hiển thị: ")
            display_by_class(students, class_name)
        elif choice == '6':
            name = input("Nhập tên sinh viên cần hiển thị: ")
            display_by_name(students, name)
        elif choice == '7':
            class_name = input("Nhập lớp cần lưu: ")
            save_students_by_class(students, class_name)
        elif choice == '8':
            print("Thoát chương trình.")
            break
        else:
            print("Chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()
