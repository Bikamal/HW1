alphabet_pattern="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 6) and (column > 1 and column < 5))):    
            alphabet_pattern=alphabet_pattern+"*"    
        else:      
            alphabet_pattern=alphabet_pattern+" "    
    alphabet_pattern=alphabet_pattern+"\n"    
print(alphabet_pattern);