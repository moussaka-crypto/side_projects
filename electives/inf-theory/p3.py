import math
from decimal import Decimal

def Z_statistik(text_file):
    
    with open(text_file, 'r', encoding="utf-8") as file:
        text = file.read()
    
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    total_chars = sum(char_count.values())
    
    probs = {}
    info_content = {}
    for char, count in char_count.items():
        probs[char] = Decimal(count) / Decimal(total_chars)
        
    return probs

#probabilities = { 'a': 1/2, 'b': 1/4, 'c': 1/8, 'd': 1/16, 'e': 1/16 }
probabilities = Z_statistik("test.txt")

with open("test.txt", 'r', encoding="utf-8") as file:
    w = file.read()

def Q_ACencoder(word):
    low = 0
    high = 1
    
    prev_start = low
    
    counter = 0
    builder = []
    
    for c in word:
        start = prev_start
        delta = high - low
        
        for a,p in probabilities.items():
            prev_start = start
            start = Decimal(start) + Decimal(delta) * Decimal(p)
            
            print("P: ",prev_start)
            print("S: ",start)
            
            if c != a:
                continue
            
            print(a, (prev_start+start)/2)
            
            
            
            if counter != 0 and counter % 20 == 0:
                builder.append(Decimal((low+high)/2))
                prev_start = 0
                start = 1
            
            counter = counter + 1
            
            
            low = prev_start
            high = start
            start = prev_start
            break
    
    builder.append(Decimal((low+high)/2))
    
    return builder

def Q_ACdecoder(code):
    low = 0
    high = 1
    
    build_word = ""
    
    counter = 0
    
    for c in code:
        
        prev_start = 0
        start = 1
        
        low = prev_start
        high = start
        start = prev_start
        
        while c != Decimal((high+low)/2):
            start = prev_start
            delta = high - low
        
            for a,p in probabilities.items():
                prev_start = start
                start = Decimal(start) + Decimal(delta) * Decimal(p)
            
                if not(prev_start <= c and start > c):
                    continue
                
                print(build_word)
                build_word += a
                
                
                
                
                if counter != 0 and counter % 20 == 0:
                    prev_start = 0
                    start = 1
                
                counter = counter + 1
                
                
                low = prev_start
                high = start
                start = prev_start
                break    
    
    return build_word

enc = Q_ACencoder(w)
print(enc)
dec = Q_ACdecoder(enc)
print(dec)
