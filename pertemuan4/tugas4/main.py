from tabulate import tabulate
from kurs import data_kurs
from konverter import hitung_konversi

def tampilkan_tabel():
    headers = ["Kode", "Kurs"]
    table_data = [[key, f"{value:,}"] for key, value in data_kurs.items()]
    print("\n=== KONVERTER MATA UANG ===")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def main():
    tampilkan_tabel()
    
    dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
    ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
    jumlah = float(input("Jumlah: "))
    
    hasil = hitung_konversi(dari, ke, jumlah)
    
    simbol_dari = "Rp " if dari == "IDR" else f"{dari} "
    
    print(f"{simbol_dari}{jumlah:,} = {hasil:,.2f} {ke}")

if __name__ == "__main__":
    main()