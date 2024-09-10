with open ("turkce_kelime_listesi.txt","r", encoding = "utf-8") as dosya:
    liste =[satir.strip() for satir in dosya.readlines()]

print(liste)

