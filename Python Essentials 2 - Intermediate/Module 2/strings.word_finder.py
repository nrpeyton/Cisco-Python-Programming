def find_word(string1, string2):
    for c in string1:
        if string2.find(c) > -1:     # .find() returns -1 if not found
            result = 'Yes'
        else:
            return 'No'
    
    return result
            
    


print(find_word('a', 'bcd'))
print(find_word('donor', 'Nabucodonosor'))
print(find_word('donut', 'Nabucodonosor'))