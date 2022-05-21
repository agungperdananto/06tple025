def down(x, xmin, xmax):
    return (xmax- x) / (xmax - xmin)

def up(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)

class Permintaan():
    minimum = 2100
    maximum = 3500

    def turun(self, x):
        if x >= self.maximum:
            return 0
        elif x <= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x <= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)

class Persediaan():
    minimum = 100
    medium = 300
    maximum = 500

    def sedikit(self, x):
        if x >= self.medium:
            return 0
        elif x <= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.medium)
    
    def cukup(self, x):
        if self.minimum < x < self.medium:
            return up(x, self.minimum, self.medium)
        elif self.medium < x < self.maximum:
            return down(x, self.medium, self.maximum)
        elif x == self.medium:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.maximum:
            return 1
        elif x <= self.medium:
            return 0
        else:
            return up(x, self.medium, self.maximum)

class Produksi():
    minimum = 1000
    maximum = 5000
    
    def kurang(self, α):
        return self.maximum - α * (self.maximum-self.minimum)

    def tambah(self, α):
        return α *(self.maximum - self.minimum) + self.minimum

    # 2 permintaan 3 persediaan
    def inferensi(self, jumlah_permintaan, jumlah_persediaan):
        pmt = Permintaan()
        psd = Persediaan()
        result = []
        # [R1] JIKA Permintaan TURUN, dan Persediaan BANYAK, 
        #     MAKA Produksi Barang BERKURANG.
        α1 = min(pmt.turun(jumlah_permintaan), psd.banyak(jumlah_persediaan))
        z1 = self.kurang(α1)
        result.append((α1, z1))
        # [R2] JIKA Permintaan TURUN, dan Persediaan SEDIKIT, 
        #     MAKA Produksi Barang BERKURANG.
        α2 = min(pmt.turun(jumlah_permintaan), psd.sedikit(jumlah_persediaan))
        z2 = self.kurang(α2)
        result.append((α2, z2))
        # [R3] JIKA Permintaan NAIK, dan Persediaan BANYAK, 
        #     MAKA Produksi Barang BERTAMBAH.
        α3 = min(pmt.naik(jumlah_permintaan), psd.banyak(jumlah_persediaan))
        z3 = self.tambah(α3)
        result.append((α3, z3))
        # [R4] JIKA Permintaan NAIK, dan Persediaan SEDIKIT,
        #     MAKA Produksi Barang BERTAMBAH.
        α4 = min(pmt.naik(jumlah_permintaan), psd.sedikit(jumlah_persediaan))
        z4 = self.tambah(α4)
        result.append((α4, z4))

        # [R5] JIKA Permintaan NAIK, dan Persediaan CUKUP,
        #     MAKA Produksi Barang BERKURANG.
        α5 = min(pmt.naik(jumlah_permintaan), psd.cukup(jumlah_persediaan))
        z5 = self.kurang(α5)
        result.append((α5, z5))

        # [R6] JIKA Permintaan NAIK, dan Persediaan CUKUP,
        #     MAKA Produksi Barang BERKURANG.
        α6 = min(pmt.turun(jumlah_permintaan), psd.cukup(jumlah_persediaan))
        z6 = self.tambah(α6)
        result.append((α6, z6))

        return result
    
    def defuzifikasi(self, jumlah_permintaan, jumlah_persediaan):
        inferensi_values = self.inferensi(jumlah_permintaan, jumlah_persediaan)
        return sum([(value[0]* value[1]) for value in inferensi_values]) / sum([value[0] for value in inferensi_values])