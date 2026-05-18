"""
Jadi di kode ini hanya perlu untuk memasukkan nilai piutang awal, anuitas,. 
Setelah itu, program akan menghitung sisa piutang, bunga, dan angsuran untuk setiap periode hingga piutang habis atau menjadi negatif.
Bunga jika dalam bentuk persen (2.1%) bagi 100 agar menjadi desimal (0.021) untuk perhitungan.
dan (0.021) bentuk desimal dan bisa di in[ut di program langsung.
"""

print("=== Program Perhitungan Piutang dan Anuitas ===")
print("=" * 30)
piutang= int(input("Masukkan Piutang Awal: "))
anuitas = int(input("Masukkan Anuitas: "))
bunga = float(input("Masukkan Bunga: "))
print("=" * 30)

periode = 1
while piutang >= 0:
        bunga_b = piutang * bunga
        angsuran = anuitas - bunga_b
        sisa = piutang - angsuran
        
       
        print("="* 30)
        print(f"\nPeriode {periode}: \nPiutang = {piutang:.2f} \nBunga = {bunga_b:.2f} \nAngsuran = {angsuran:.2f} \nSisa = {sisa:.2f}")
   
        periode += 1
        piutang = sisa
        if sisa < 0:
           print("="*50)
        
           print(f"Notes: Lakukan Ini Jika Sudah  Di Periode {periode - 1}")
           print("- Sisa Diganti 0")
           print(f"- Dan Angsuran Diganti Piutang Periode Ke {periode - 1}\n")
           print("="*50)

            
#Jika Sisa - Di Akhir == 0




