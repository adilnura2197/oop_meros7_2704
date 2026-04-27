#28
class Kurs:
    def __init__(self, nomi):
        self.nomi = nomi

    def boshlash(self):
        print("Kurs boshlandi", end=" ")


class PythonKurs(Kurs):
    def boshlash(self):
        super().boshlash()
        print(", Python kurs boshlandi")


k1 = Kurs("Ingliz tili")
p1 = PythonKurs("IT")

k1.boshlash()
p1.boshlash()


#29
class Uy:
    def __init__(self, manzil):
        self.manzil = manzil

    def info(self):
        print("Uy mavjud", end=" ")


class Villa(Uy):
    def info(self):
        super().info()
        print(", Bu villa")


u1 = Uy("Yoshlik")
v1 = Villa("Navbahor")

u1.info()
v1.info()
