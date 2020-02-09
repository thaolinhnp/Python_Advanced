class PhuongTrinhBacNhat():
    def __init__(self, _a, _b):
        self.a = _a
        self.b = _b
    def NghiemPhuongTrinh(self):
        if self.a == 0 and self.b != 0:
            x = 'vo nghiem'
        elif self.b == 0:
            x = ' vo so nghiem'
        else:
            x = -self.b/self.a
        return x
    def KetQua(self):
        print('Ket qua:', self.NghiemPhuongTrinh())

if __name__ == "__main__":
    ptbn = PhuongTrinhBacNhat(0,2)
    print('Nghiem cua phuong trinh là',ptbn.NghiemPhuongTrinh())
    print(ptbn.KetQua())