kingdom_dict = {
    "LAND": "PANDA",
    "WATER": "OCTOPUS",
    "ICE": "MAMMOTH",
    "AIR": "OWL",
    "FIRE": "DRAGON"
}


def Decrypt_Message(message):
    msgList = message.split(" ")
    kingdom = msgList[0]
    sec_msg = msgList[1]
    key = kingdom_dict[kingdom] #name of kindom
    l = len(key) #length of the kingdom
    dm = caesarCipherEncryptor(sec_msg, l)
    print(sec_msg, dm, l)
    return dm


def caesarCipherEncryptor(string, key):
    # Write your code here.
    newLetter = []
    newKey = key % 26
    for letter in string:
        newLetter.append(getNewLatter(letter, newKey))
    return "".join(newLetter)


def getNewLatter(letter, newKey):
    newLetterCode = ord(letter) + newKey
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode %122)


print(Decrypt_Message("AIR ROZO"))

print(ord("a"))
print(chr(122))