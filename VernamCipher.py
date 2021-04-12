def makeVernamCypher( text, key ):
    """ Returns the Vernam Cypher for given string and key """
    answer = ""              # the Cypher text
    p = 0                    # pointer for the key
    for char in text:
        answer += chr(ord(char) ^ ord(key[p]))
        p += 1
        if p==len(key):
            p = 0
    return answer

                      
MY_KEY = "djjsjai1949v,dk3fkkkqvbsrh"
while True:
   
    PlainText = input("Enter text to encrypt: ")
    # Encrypt
    Cypher = makeVernamCypher(PlainText, MY_KEY)
    print("Cypher text: "+Cypher)
    # Decrypt
    decrypt = makeVernamCypher(Cypher, MY_KEY)
    print("Decrypt: "+decrypt)
