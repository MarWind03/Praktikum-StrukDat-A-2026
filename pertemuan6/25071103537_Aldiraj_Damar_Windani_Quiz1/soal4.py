level_diskon = ( 
    (500000, 15),   # belanja >= 500.000 -> diskon 15% 
    (300000, 10),   # belanja >= 300.000 -> diskon 10% 
    (100000,  5),   # belanja >= 100.000 -> diskon  5% 
    (0,        0),  # default            
)

def hitung_diskon(total_belanja, level_diskon, index=0):
    belanja, diskon = level_diskon[index]
    if total_belanja >= belanja:
        nominal_diskon = total_belanja*diskon/100
        return (diskon, nominal_diskon, total_belanja-nominal_diskon)
    else:
        return hitung_diskon(total_belanja, level_diskon, index+1)

nama = input("Masukkan nama item belanja : ")
total_belanja = int(input("Masukkan total belanja : "))
data_belanja = hitung_diskon(total_belanja, level_diskon)
diskon, nominal_diskon, total_bayar = data_belanja
if total_belanja < 100000:
    print("Tidak ada diskon.")

print(f"Total Belanja : {total_belanja}")
print(f"Persen Diskon : {diskon}")
print(f"Nominal Diskon : {nominal_diskon}")
print(f"Total Bayar : {total_bayar}")