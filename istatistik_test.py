from Mat_İstatistik import Mat,İstatistik
import pytest

def girdi_test():
    tekSayılıkVeri = İstatistik(1)
    with pytest.raises(ValueError):
        tekSayılıkVeri(1)
