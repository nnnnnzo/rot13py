def rot13(Clair):
    crypt = ""
    for r in Clair :
        if r != " ":
            result = ord(r)+13
            if result > 122 :    crypt += chr(result - 26)
            else:   crypt += chr(result)
        else :  crypt += " "
    print(crypt)
        
def rot13file():
    crypt = ""
    f = open("tocrypt.txt", "r")
    e = open("crypted.txt", "w")
    for d in f :
        for r in d:
            if r != " ":
                result = ord(r)+13
                if result > 122 :    crypt += chr(result - 26)
                else:   crypt += chr(result)
            else :  crypt += " "
    e.write(crypt)
    f.close
