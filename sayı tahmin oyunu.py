import random
import time

print("""
********************************************************************

	  1 ile 100 arasındaki gizli sayıyı tahmin etme oyunu


********************************************************************""")

rasgele_sayı=random.randint(1,100)
tahmin_hakkı=5
kullanıcı=input("İsminizi Girin:")
while True:
	tahmin=int(input("Tahmin Giriniz:"))	
	if tahmin<rasgele_sayı:
		print("Bilgiler sorgulanıyor...")
		time.sleep(1)

		print("Daha yüksek bir sayı söyleyiniz...")

		tahmin_hakkı-=1

	elif tahmin>rasgele_sayı:
		print("Bilgiler sorgulanıyor...")
		time.sleep(1)

		print("Daha düşük bir sayı söyleyiniz...")

		tahmin_hakkı-=1
	else:
		print("Bilgiler sorgulanıyor...")
		time.sleep(1)

		print("Tebrikler",kullanıcı," gizli sayımız",rasgele_sayı)
		break
	if tahmin_hakkı==0:
		print("Tahmin hakkınız bitti")
		print(" gizli sayımız",rasgele_sayı)
		break