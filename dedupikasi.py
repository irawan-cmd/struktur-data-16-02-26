def deduplikasi(data):
    sudah_ada = set()
    hasil = []
    
    for item in data:
        if item not in sudah_ada:
            sudah_ada.add(item)
            hasil.append(item)
            
    return hasil

# Contoh
print(deduplikasi([1,2,2,3,4,1,5]))
