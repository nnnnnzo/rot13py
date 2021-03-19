#rot13() --> TP 1,2,3 // rot13file() --> TP 4

def rot13(Clair):
    crypt = ""
    for r in Clair : # pour chaque caractères
        if r != " ": # si le caractère est un espace
            result = ord(r)+13 # on converti le caractères en ascii + 13
            if result > 122 :    crypt += chr(result - 26) # si le ascii est > 122; on revient au début de l'alphabet
            else:   crypt += chr(result) # on rajoute la lettre crypté au texte crypté final
        else :  crypt += " " # si un espace on ajoute un espace
    print(crypt) # affiche le texte crypté 
        
def rot13file():
    crypt = ""
    f = open("tocrypt.txt", "r") # ouvre tocrypt.txt en lecture
    e = open("crypted.txt", "w") # ouvre crypted.txt en écriture
    for d in f : #pour le texte dans le fichier f
        for r in d: # pour le caractère dans le texte du fichier f
            if r != " ": # si le caractère est un espace
                result = ord(r)+13 # on converti le caractères en ascii + 13
                if result > 122 :    crypt += chr(result - 26) # si le ascii est > 122; on revient au début de l'alphabet
                else:   crypt += chr(result) # on rajoute la lettre crypté a la variable du texte crypté final
            else :  crypt += " " # si un espace on ajoute un espace
    e.write(crypt) # on write la valeur de la variable crypt dans le fichier crypted.txt
    f.close # on ferme le fichier f
    e.close # on ferme le fichier e

    def rot13fileuncrypt():
    uncrypt = ""
    f = open("todecrypt.txt", "r") # ouvre todecrypt.txt en lecture
    e = open("uncrypted.txt", "w") # ouvre uncrypted.txt en écriture
    for d in f : #pour le texte dans le fichier f
        for r in d: # pour le caractère dans le texte du fichier f
            if r != " ": # si le caractère est un espace
                result = ord(r)-13 # on converti le caractères en ascii - 13
                if result < 97 :    uncrypt += chr(result + 26) # si le ascii est < 97; on revient a la fin de l'alphabet
                else:   uncrypt += chr(result) # on rajoute la lettre decrypté a la variable du texte decrypté final
            else :  uncrypt += " " # si un espace on ajoute un espace
    e.write(uncrypt) # on write la valeur de la variable crypt dans le fichier crypted.txt
    f.close # on ferme le fichier f
    e.close # on ferme le fichier e
    
def v(txt):
    cle = "cledetest"
    eg = []
    crypt=""
    for i in range(len(txt)):
        eg.append(cle[i%len(cle)])
    print(eg)
    for i in range(len(txt)):
        crypt=chr((((ord(txt[i]%97)+(ord(eg[i])%97))%26)+97))
    print(crypt)
