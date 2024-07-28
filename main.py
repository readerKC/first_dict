meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek"
            }
        
talep = input("Hangi kelimeyi öğrenmek istersiniz?")

if talep in meme_dict.keys():
    print("Girdiğiniz kelimenin anlamı: ", meme_dict[talep])
else:
    print("Üzgünüm bu sözlükte aradığınız kelime yok:(")
