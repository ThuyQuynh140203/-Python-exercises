class HoGiaDinh:
    def __init__(self, so_phong, so_toa_nha, chu_ho, so_kwh):
        self.so_phong = so_phong
        self.so_toa_nha = so_toa_nha
        self.chu_ho = chu_ho
        self.so_kwh = so_kwh
        self.tien_dien = 0

    def hienThi(self):
        tien_dien_full = self.tien_dien * 1.1  # Cộng thêm 10% thuế VAT
        print(
            f"{self.so_toa_nha:<10} {self.so_phong:<10} {self.so_kwh:<20} {tien_dien_full:} VND")


def nhapThongTin():
    dsHoGiadinh = []

    while True:
        so_phong = input('Nhập số phòng: ').strip()
        so_toa_nha = input('Nhập số hiệu tòa nhà: ').strip()
        chu_ho = input('Nhập tên chủ hộ: ').strip()
        so_kwh = float(input('Nhập số kWh: '))

        if so_phong and so_toa_nha and chu_ho and so_kwh >= 0:
            ho = HoGiaDinh(so_phong, so_toa_nha, chu_ho, so_kwh)
            dsHoGiadinh.append(ho)
            print('Thêm hộ gia đình thành công')
        else:
            print('Thêm hộ gia đình thất bại')

        tiep_tuc = input('Bạn có muốn tiếp tục thêm hộ gia đình không (y/n): ')
        if tiep_tuc.lower() == 'n':
            break
    return dsHoGiadinh


def tinhtiendien(kwh):
    if kwh <= 50:
        return kwh * 1678
    elif kwh <= 100:
        return 50 * 1678 + (kwh - 50) * 1734
    elif kwh <= 200:
        return 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
    elif kwh <= 300:
        return 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 200) * 2536
    elif kwh <= 400:
        return 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (kwh - 300) * 2834
    else:
        return 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834 + (kwh - 400) * 2927


def hienThiThongTin(dsHoGiaDinh):
    print(f"{'Tòa nhà':<10} {'Phòng':<10} {'Số kWh':<20} {'Tiền điện':<20}")
    for ho in dsHoGiaDinh:
        ho.tien_dien = tinhtiendien(ho.so_kwh)
        ho.hienThi()  # Hiển thị thông tin của hộ gia đình

def ghi_file(dsHoGiadinh):
    for ho in dsHoGiadinh:
        ten_file = f'{ho.so_toa_nha}.txt'
        tien_dien = ho.tien_dien
        with open(ten_file, 'w+', encoding='utf-8') as file:
            file.write(f'f"Tòa nhà: {ho.so_toa_nha}, Phòng: {ho.so_phong}, Chủ hộ: {ho.chu_ho}, Số kWh: {ho.so_kwh}, Tiền điện: {tien_dien:} VND\n')

def menu():
    dsHoGiadinh = []

    while True:
        print("\nChọn tùy chọn:")
        print("1. Nhập thông tin hộ gia đình")
        print("2. Hiển thị danh sách hộ gia đình")
        print("3. Luu vào file")
        print('4. Thoat')
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            dsHoGiadinh.extend(nhapThongTin())
        elif choice == '2':
            hienThiThongTin(dsHoGiadinh)
        elif choice == '3':
            ghi_file(dsHoGiadinh)
        elif choice == '4':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == '__main__':
    menu()
