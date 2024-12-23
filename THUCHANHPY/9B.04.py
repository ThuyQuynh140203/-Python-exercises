import os

class MonHoc:
    def __init__(self, maMon, tenMon, tinChi):
        self.maMon = maMon
        self.tenMon = tenMon
        self.tinChi = tinChi

    def __str__(self):
        return f"{self.maMon} | {self.tenMon} | {self.tinChi}"

class QuanLyMonHoc:
    def __init__(self):
        self.dsMonHoc = []

    def themMon(self, maMon, tenMon, tinChi):
        mon_hoc = MonHoc(maMon, tenMon, tinChi)
        self.dsMonHoc.append(mon_hoc)
        print("Them mon hoc thanh cong")

    def xoaMon(self, maMon):
        for monHoc in self.dsMonHoc:
            if monHoc.maMon == maMon:
                self.dsMonHoc.remove(monHoc)
                print("Xoa mon hoc thanh cong")
                return
        print("Khong tim thay ma mon hoc can xoa")

    def hienThiDsMonHoc(self):
        print(f"{'Mã môn':<15}{'Ten mon hoc':<30}{'So tin chi'}")
        for mon_hoc in self.dsMonHoc:
            print(f"{mon_hoc.maMon:<15}{mon_hoc.tenMon:<30}{mon_hoc.tinChi}")

    def timKiemMonHoc(self, loai: str, tu_khoa: str):
        ketqua = []
        if loai == "ma":
            for mh in self.dsMonHoc:
                if tu_khoa.strip().lower() == mh.maMon.strip().lower():
                    ketqua.append(mh)
        elif loai == "ten":
            for mh in self.dsMonHoc:
                if tu_khoa.lower() == mh.tenMon.lower():
                    ketqua.append(mh)
        elif loai == "tin":
            try:
                tin_chi = int(tu_khoa)
                for mh in self.dsMonHoc:
                    if tin_chi == mh.tinChi:
                        ketqua.append(mh)
            except ValueError:
                print("Số tín chỉ không hợp lệ.")
                return

        # Hiển thị kết quả tìm kiếm
        if ketqua:
            print(f"{'Mã môn học':<15}{'Tên môn học':<30}{'Số tín chỉ':<10}")
            for mh in ketqua:  # Vòng lặp này hiển thị các môn học tìm được
                print(f"{mh.maMon:<15}{mh.tenMon:<30}{mh.tinChi:<10}")
        else:
            print("Không tìm thấy môn học phù hợp.")

    def ghi_tap_tin(self, file_name):
        """Ghi danh sách môn học vào tập tin."""
        with open(file_name, 'w', encoding='utf-8') as file:
            for mon_hoc in self.dsMonHoc:
                file.write(str(mon_hoc) + "\n")
        print("Ghi dữ liệu vào tập tin thành công!")

    def doc_tap_tin(self, file_name):
        """Đọc danh sách môn học từ tập tin."""
        self.dsMonHoc.clear()  # Xóa sạch danh sách trước khi đọc dữ liệu mới
        if os.path.exists(file_name):  # Kiểm tra xem file có tồn tại không
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    ma_mon, ten_mon, so_tin_chi = line.strip().split('|')
                    self.dsMonHoc.append(MonHoc(ma_mon, ten_mon, int(so_tin_chi)))
            print("Đọc dữ liệu từ tập tin thành công!")
        else:
            print("Tập tin không tồn tại.")

def main():
    ql_mon_hoc = QuanLyMonHoc()

    while True:
        print("\nChuong trinh quan ly mon hoc")
        print("1. Them mon hoc")
        print("2. Xoa mon hoc")
        print("3. Hien thi danh sach mon hoc")
        print("4. Tim kiem mon hoc")
        print("5. Ghi du lieu vao tap tin")
        print("6. Doc du lieu tu tap tin")
        print("7. Thoat")

        choice = input("Nhap lua chon: ")
        if choice == "1":
            ma = input("Nhap ma mon: ")
            ten = input("Nhap ten mon: ")
            tinChi = input("Nhap so tin chi: ")
            ql_mon_hoc.themMon(ma, ten, tinChi)
        elif choice == "2":
            ma = input("Nhap ma mon hoc: ")
            ql_mon_hoc.xoaMon(ma)
        elif choice == "3":
            ql_mon_hoc.hienThiDsMonHoc()
        elif choice == "4":
            loai = input("Chon loai tim kiem (ma/ten/tin): ")
            tu_khoa = input("Nhap tu khoa: ")
            ql_mon_hoc.timKiemMonHoc(loai, tu_khoa)
        elif choice == "5":
            file_name = input("Nhap ten tap tin: ")
            ql_mon_hoc.ghi_tap_tin(file_name)
        elif choice == "6":
            file_name = input("Nhap ten tap tin: ")
            ql_mon_hoc.doc_tap_tin(file_name)
        elif choice == "7":
            print("Thoat chuong trinh.")
            break  # Thoát chương trình

main()
