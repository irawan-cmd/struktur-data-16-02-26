def first_recurring_char(teks):
    sudah_ada = set()
    
    for huruf in teks:
        if huruf in sudah_ada:
            return huruf
        sudah_ada.add(huruf)
    
    return None

# Contoh
print(first_recurring_char("programming"))
