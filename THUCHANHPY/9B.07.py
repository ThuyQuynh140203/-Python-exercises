class MonHoc:
    def __init__(self, ma_mon, ten_mon, so_tiet):
        self.ma_mon = ma_mon
        self.ten_mon = ten_mon
        self.so_tiet = so_tiet


class HocVien:
    def __init__(self, so_cccd, ten, nam_sinh):
        self.so_cccd = so_cccd
        self.ten = ten
        self.nam_sinh = nam_sinh
        self.danh_sach_mon_hoc = []

    def dang_ky_mon_hoc(self, mon_hoc):
        self.danh_sach_mon_hoc.append(mon_hoc)

    def hien_thi_thong_tin(self):
        print(f"Số CCCD/Mã số giấy khai sinh: {self.so_cccd}")
        print(f"Tên học viên: {self.ten}")
        print(f"Năm sinh: {self.nam_sinh}")
        print("Danh sách các môn học:")
        for mon in self.danh_sach_mon_hoc:
            print(f"  - Mã môn học: {mon.ma_mon}, Tên môn học: {mon.ten_mon}, Số tiết: {mon.so_tiet}")


def luu_thong_tin_hoc_vien(ten_file, danh_sach_hoc_vien):
    with open(ten_file, 'w') as file:
        for hv in danh_sach_hoc_vien:
            file.write(f"{hv.so_cccd},{hv.ten},{hv.nam_sinh}\n")
            for mon in hv.danh_sach_mon_hoc:
                file.write(f"  {mon.ma_mon},{mon.ten_mon},{mon.so_tiet}\n")
    print(f"Thông tin học viên đã được ghi thành công vào tệp {ten_file}")


def hien_thi_ds_hoc_vien(danh_sach_hoc_vien):
    for hv in danh_sach_hoc_vien:
        hv.hien_thi_thong_tin()


def hien_thi_hv_2_mon(danh_sach_hoc_vien):
    for hv in danh_sach_hoc_vien:
        if len(hv.danh_sach_mon_hoc) >= 2:
            hv.hien_thi_thong_tin()


def menu():
    danh_sach_hoc_vien = []

    while True:
        print("\nChọn một tùy chọn:")
        print("1. Nhập thông tin học viên")
        print("2. Hiển thị thông tin học viên đã đăng ký")
        print("3. Hiển thị thông tin học viên đăng ký ít nhất 2 môn học")
        print("4. Lưu thông tin học viên vào tệp DSHV.txt")
        print("5. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            so_cccd = input("Nhập số CCCD/Mã số giấy khai sinh: ")
            ten = input("Nhập tên học viên: ")
            nam_sinh = int(input("Nhập năm sinh: "))
            hoc_vien = HocVien(so_cccd, ten, nam_sinh)

            so_mon_hoc = int(input("Nhập số môn học học viên đăng ký: "))
            for _ in range(so_mon_hoc):
                ma_mon = input("Nhập mã môn học: ")
                ten_mon = input("Nhập tên môn học: ")
                so_tiet = int(input("Nhập số tiết: "))
                hoc_vien.dang_ky_mon_hoc(MonHoc(ma_mon, ten_mon, so_tiet))

            danh_sach_hoc_vien.append(hoc_vien)
        elif choice == '2':
            hien_thi_ds_hoc_vien(danh_sach_hoc_vien)
        elif choice == '3':
            hien_thi_hv_2_mon(danh_sach_hoc_vien)
        elif choice == '4':
            luu_thong_tin_hoc_vien('DSHV.txt', danh_sach_hoc_vien)
        elif choice == '5':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == '__main__':
    menu()
