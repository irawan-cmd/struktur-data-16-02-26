def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    hitung = {}
    
    for huruf in s1:
        hitung[huruf] = hitung.get(huruf, 0) + 1
        
    for huruf in s2:
        if huruf not in hitung:
            return False
        hitung[huruf] -= 1
        if hitung[huruf] < 0:
            return False
            
    return True

# Contoh
print(is_anagram("listen", "silent"))
