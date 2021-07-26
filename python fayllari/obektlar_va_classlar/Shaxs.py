class Shaxs:
    def __init__(self, ism, fam,shaxri,mahallasi):
        self.ism = ism
        self.fam = fam
        self.shaxri = shaxri
        self.mahallasi = mahallasi

    def tuliq_ism(self):
        return self.ism + ' ' + self.fam

    def adres(self):
        return self.shaxri + ' ' + self.mahallasi


xodim = Shaxs("Jahongir", "Jumanov","Baxmal tumani","Mo'g'ol qishlog'i")
print(xodim.tuliq_ism(),xodim.adres())