kilo = int(input("masukan berapa kilo :"))

harga_2kg = 20_000 
#harga 3kg-5kg perkilo
harga_5kg = 18_000
harga_per_kilo = 16_000

if kilo <=2 :
    total_harga = harga_2kg 
elif kilo <=5 :
    total_harga = harga_5kg * kilo
else :
    total_harga = harga_per_kilo * kilo

print("harga yang harus dibayar unutk membeli ",kilo,"kg mangga adalah",total_harga,"")

