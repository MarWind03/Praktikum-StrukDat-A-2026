from kurs import data_kurs

def hitung_konversi(dari, ke, jumlah):
    # Konversi asal ke IDR 
    jumlah_idr = jumlah * data_kurs[dari]
    
    # Konversi dari IDR ke target
    hasil = jumlah_idr / data_kurs[ke]
        
    return hasil