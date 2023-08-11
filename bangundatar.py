def rumus():
    print("=" * 35)
    print("OPERASI MENGHITUNG LUAS BANGUN DATAR")
    print("Silahkan Pilih : ")
    print("1. SEGITIGA")
    print("2. PERSEGI PANJANG")
    print("3. PERSEGI")
    print("4. LINGKARAN")
    print("5. LIMAS")

    print("=" * 35)

    bangundatar = input('Pilih Bangun datar 1/2/3/4 : ')
    if bangundatar == '1':
            print("Luas SEGITIGA : ")
            alas = eval(input("Masukkan alas : "))
            tinggi = eval(input("Masukkan tinggi : "))
            hasil = 1/2 * alas * tinggi
            print(f'Hasil dari perhitungan luas Segitiga adalah : {1/2} * {alas} * {tinggi} = {hasil}')
    elif bangundatar == '2':
            print("Luas PERSEGI PANJANG : ")
            panjang = eval(input("Masukkan panjang : "))
            lebar = eval(input("Masukkan lebar : "))
            hasil = panjang * lebar
            print(f'Hasil dari perhitungan luas persegi panjang adalah : {panjang} * {lebar} = {hasil}')
    elif bangundatar == '3':
            print("Luas PERSEGI : ")
            sisi_1 = eval(input("Masukkan Sisi 1 : "))
            sisi_2 = eval(input("Masukkan Sisi 2 : "))
            hasil = sisi_1 * sisi_2
            print(f'Hasil dari perhitungan luas persegi adalah : {sisi_1} * {sisi_2} = {hasil}')
    elif bangundatar == "4":
            print("Luas LINGKARAN : ")
            phi = eval(input('Masukkan π : '))
            jarijari = eval(input('Masukkan jari jari : '))
            hasil = phi * jarijari ** 2
            print(f'Hasil dari perhitungan luas Lingkaran adalah : {phi} * {jarijari} ** {2} = {hasil}')
    elif bangundatar == "5":
            print("Luas LIMAS : ")
            luasalas = eval(input("Masukkan Luas alas : "))
            luassisitegak = eval(input("Masukkan Luas sisi tegak : "))
            hasil = luasalas + luassisitegak
            print(f'Hasil dari perhitungan luas Limas adalah : {luassisitegak} + {luasalas} = {hasil}')
    else :
            print("Maaf kami tidak bisa memproses permintaan anda untuk saat ini\nkami akan mengembangkan aplikasi ini. TERIMAKASIH")
rumus()

reset= input("apakah ingin mengulang program? :")
if reset == "ya":
       rumus()
else:
       print("terima kasih")