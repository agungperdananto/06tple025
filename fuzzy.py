class Permintaan():
    minimum = 1000
    maximum = 5000

    def turun(self, x):
        if x >= self.maximum:
            return 0
        elif x <= self.minimum:
            return 1
        else:
            return (self.maximum - x) / (self.maximum - self.minimum)

    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x <= self.minimum:
            return 0
        else:
            return (x - self.minimum) / (self.maximum - self.minimum)

class Persediaan():
    minimum = 100
    maximum = 600

    def sedikit(self, x):
        if x >= self.maximum:
            return 0
        elif x <= self.minimum:
            return 1
        else:
            return (self.maximum - x) / (self.maximum - self.minimum)

    def banyak(self, x):
        if x >= self.maximum:
            return 1
        elif x <= self.minimum:
            return 0
        else:
            return (x - self.minimum) / (self.maximum - self.minimum)

class Produksi():
    minimum = 2000
    maximum = 7000
    
    def kurang(self, α):
        return self.maximum - α * (self.maximum-self.minimum)

    def tambah(self, α):
        return α *(self.maximum - self.minimum) + self.minimum

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
        return result
    
    def defuzifikasi(self, jumlah_permintaan, jumlah_persediaan):
        inferensi_values = self.inferensi(jumlah_permintaan, jumlah_persediaan)
        return sum([(value[0]* value[1]) for value in inferensi_values]) / sum([value[0] for value in inferensi_values])
# Permintaan = 4000 & Persediaan 300


# https://www.slideshare.net/ZaenalKhayat/contoh-peyelesaian-logika-fuzzy