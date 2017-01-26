def alphabet_position(letter):
    for i in letter:
        char = ord(i)
        if char >= 97:
            charPos = char - 97
            return charPos
        if char < 97:
            charPos = char - 65
            return charPos

#rotate the character
def rotate_character(char, rot):
    if char.isalpha():
        charPos = alphabet_position(char)
        newPos = (int(charPos) + int(rot)) % 26
        char = ord(char)
        if char >= 97:
            if char <= 122:
                newPos = chr(newPos + 97)
                return newPos
        if char <= 98:
            if char >= 65:
                newPos = chr(newPos + 65)
                return newPos
    else:
        return char

def encrypt(text, rot):
    new_string = ''
    for i in text:
        new_string = new_string + rotate_character(i, rot)
    return new_string
