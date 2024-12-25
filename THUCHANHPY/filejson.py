import json

class SinhVien:
    def __init__(self, ho, ten, ma_sv, ma_lop, gioi_tinh, diem_so):
        self.ho = ho
        self.ten = ten
        self.ma_sv = ma_sv
        self.ma_lop = ma_lop
        self.gioi_tinh = gioi_tinh
        self.diem_so = {diem['name']: diem['score'] for diem in diem_so}

    def lay_ten(self):
        return f"{self.ho} {self.ten}"

    def lay_diem(self, mon_hoc):
        return self.diem_so.get(mon_hoc, 0)

    def thay_doi_diem(self, mon_hoc, diem):
        if mon_hoc in self.diem_so:
            self.diem_so[mon_hoc] = diem
        else:
            print(f"Không tìm thấy môn học {mon_hoc}!")

    def diem_cao_nhat(self):
        return max(self.diem_so.values())

    def diem_thap_nhat(self):
        return min(self.diem_so.values())

    def diem_trung_binh(self):
        return sum(self.diem_so.values()) / len(self.diem_so)

    def __str__(self):
        return (f"Tên: {self.lay_ten()}\n"
                f"Điểm cao nhất: {self.diem_cao_nhat()}\n"
                f"Điểm thấp nhất: {self.diem_thap_nhat()}\n"
                f"Điểm trung bình: {self.diem_trung_binh():.2f}")

def doc_du_lieu_tu_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return [SinhVien(
            sv['first_name'],
            sv['last_name'],
            sv['id'],
            sv['st_code'],
            sv['gender'],
            sv['scores']
        ) for sv in data]

def main():
    danh_sach_sinh_vien = doc_du_lieu_tu_json('data.json')
    for sinh_vien in danh_sach_sinh_vien:
        print(sinh_vien)
        print("-" * 40)

if __name__ == '__main__':
    main()
