class ToanHoc:
    def __init__(self, *nso):
        self.nso = nso

    def tinhtong(self):
        tong = 0
        for num in self.nso:
            tong += num
        return tong

    def tinh_trung_binh(self):
        if len(self.nso) == 0:
            return 0
        tong = self.tinhtong()

        return tong / len(self.nso)
    # def tinhmax(self):