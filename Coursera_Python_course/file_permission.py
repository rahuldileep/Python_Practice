def octal_to_string(octal):
    result = ""
    value_letter = [(4,"r"),(2,"w"),(1,"x")]
    for char in str(octal):
        digit = int (char)
        for value, letter in value_letter:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------