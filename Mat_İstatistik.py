import re
class Mat:
    def __init__(self,veri):
        self._veri = None  
        self.veri = veri
    def veriAnalizi(self, veri=None):
        if veri is None:
            veri = self._veri
        veri_str = veri if isinstance(veri, str) else " ".join(map(str, veri))
        veriÖzellikleri = {
            "sayıadedi": len(re.findall(r"-?\d+\.?\d*", veri_str)),
            "birListe": isinstance(veri, list),
            "birString": isinstance(veri, str),
            "negatifSayıVar": re.search(r"-\d+", veri_str),
            "floatVar": re.search(r"\d+\.\d+", veri_str),
            "virgüllü": re.search(r",", veri_str)
        }
        return veriÖzellikleri
    @property
    def veri(self):
        return self._veri
    @veri.setter
    def veri(self, veri):
        veriÖzellikleri = self.veriAnalizi(veri)

        # Lazım olan özellikler
        birstring = veriÖzellikleri["birString"]
        birliste = veriÖzellikleri["birListe"]
        floatvar = veriÖzellikleri["floatVar"]
        virgüllü = veriÖzellikleri["virgüllü"]

        # Girilen veriyi float/int listesine çevirir [1, 2, 3, 4]
        if birstring:
            if virgüllü:
                veri = veri.replace(",", " ")
            veri = veri.split()

            try:
                if floatvar:
                    self._veri = [float(sayı) for sayı in veri]  # Listeyi doğrudan atıyoruz
                else:
                    self._veri = [int(sayı) for sayı in veri]  # Listeyi doğrudan atıyoruz
            except ValueError:
                raise ValueError("Geçersiz veri formatı. Lütfen geçerli bir sayı listesi girin.")
        elif birliste:
            try:
                if floatvar:
                    self._veri = [float(sayı) for sayı in veri]  # Listeyi doğrudan atıyoruz
                else:
                    self._veri = [int(sayı) for sayı in veri]  # Listeyi doğrudan atıyoruz
            except ValueError:
                raise ValueError("Geçersiz veri formatı. Lütfen geçerli bir sayı listesi girin.")
        else:
            raise ValueError("Veri uygun formatta değil.")
    def KareKök(self,sayı):
        return sayı**0.5

class İstatistik(Mat):
    def __init__(self,veri):
        super().__init__(veri)
    def __str__(self):
        return super().__str__()


    @property
    def veri(self):
        return self._veri
    
    @veri.setter
    def veri(self, veri):

        veriÖzellikleri = self.veriAnalizi(veri)
        sayıadedi = veriÖzellikleri["sayıadedi"]
        #Girilen veriyi float/int listesine çevirir [1,2,3,4]
        
        if sayıadedi < 2:
            raise ValueError("İstatistik İşlemleri için en az 2 sayı lazım.")
        elif sayıadedi >= 2:
            Mat.veri.fset(self, veri)

        
    
    #Sayılar listesinin Aritmetik Ortalamsını hesaplar 
    def AO(self,sayılar):
        aritmetikOrtalama = sum(sayılar) / len(sayılar)  
        return aritmetikOrtalama
    
    #Sayılar listesinin Standart Sapmasını hesaplar 
    def SS(self,sayılar):
        AritmetikOrtalama=self.AO(sayılar)
        yeniSayılar=[]
        for sayı in sayılar:
            yeniSayılar.append(super().KareKök(AritmetikOrtalama-sayı))
        SS = (sum(yeniSayılar)/(len(sayılar)-1))**2
        return SS
if __name__ == "__main__":
    veri = input("Sayıları giriniz: ")
    istatistik = İstatistik(veri)
    sayılar = istatistik.veri
    print(f"Sayıların Aritmetik Ortalaması: {istatistik.AO(sayılar)}\n Standart Sapması: {istatistik.SS(sayılar)}")