"""
Jadi kalian ubah 'piutangs' aja dan 'anuitas' sesuai soal
Kode ini situsional sesuai mood guru kalian  

"""

piutangs = 12500000 #Ubah sesuai soal
for x in range(1,15):
    piutangs -= 50000
    print(f"Absen {x+1}: Piutang = {piutangs:.2f}")

print("=" * 30)

anuitas = 1525000 #Ubah sesuai soal
for x in range(1,15):
    anuitas -= 50000
    print(f"Absen {x+1}: Anuitas = {anuitas:.2f}")
    
    
"""
Jadi for x in range(1,15) itu artinya kita akan melakukan perulangan sebanyak 14 kali,nah jadi sesuai total absen di kelas kalian ya
contoh: jika total absen di kelas kalian 20, maka kalian bisa menggunakan for x in range(1,21) karena range itu akan berhenti sebelum angka terakhir
"""
