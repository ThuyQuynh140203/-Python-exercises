def read_and_sort_students(file_name):
    students = []

    # Đọc tệp sinh viên
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            student_info = line.strip().split('|')
            students.append(student_info)

    # Sắp xếp sinh viên theo Lớp và Mã số sinh viên
    students.sort(key=lambda x: (x[3], x[0]))
    # students.sort(key=lambda x: (x[3], x[0]), reverse=True)  # Sắp xếp theo Lớp (x[3]) và Mã số (x[0])

    # Hiển thị danh sách sinh viên đã sắp xếp
    print(f"{'Mã SV':<10}{'Họ và chữ lót':<20}{'Tên':<15}{'Lớp':<10}{'Quê quán'}")
    for student in students:
        print(f"{student[0]:<10}{student[1]:<20}{student[2]:<15}{student[3]:<10}{student[4]}")

# Gọi hàm và hiển thị danh sách sinh viên từ tệp Sinhvien.txt
read_and_sort_students('Sinhvien.txt')
