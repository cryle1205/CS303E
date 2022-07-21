# File: Project2.py
# Student: Crystal Le
# UT EID: CL44964
# Course Name: CS303E
#
# Date Created: 11/7/2021
# Date Last Modified: 11/08/2021
# Description of Program: Encrypting text through a random or set key from user. The
# program can also decrypt the text as well.

import random

alphaLetters = "abcdefghijklmnopqrstuvwxyz"
upperAlpha = alphaLetters.upper()


def isLegalKey(key):
    return (len(key) == 26 and all([ch in key for ch in alphaLetters]))


def makeRandomKey():
    lst = list(alphaLetters)  # Turn string into list of letters
    random.shuffle(lst)  # Shuffle the list randomly
    return ''.join(lst)  # Assemble them back into a string


class SubstitutionCipher():
    def __init__(self, key=makeRandomKey()):
        """Create an instance of the cipher with stored key, which
        defaults to random."""
        self.__key = key

    # Note that these are the required methods, but you may define
    # additional methods if you need them.  (I didn't need any.)

    def getKey(self):
        """Getter for the stored key."""
        return self.__key

    def setKey(self, newKey):
        """Setter for the stored key.  Check that it's a legal
        key."""
        if isLegalKey(newKey) == False:
            print("Key entered is not legal")
        else:
            self.__key = newKey

    def encryptText(self, plaintext):
        """Return the plaintext encrypted with respect to the stored key."""
        encrypted = ""
        for i in range(len(plaintext)):
            if plaintext[i] == " ":
                encrypted += " "
            elif plaintext[i] == "!":
                encrypted += "!"
            elif plaintext[i] == "?":
                encrypted += "?"
            elif plaintext[i] == ".":
                encrypted += "."
            elif plaintext[i] == ",":
                encrypted += ","
            else:
                if plaintext[i].islower() == True:
                    alphaIndex = alphaLetters.find(plaintext[i])
                    lowKeyIndex = alphaIndex
                    charLowEncrypt = self.__key[lowKeyIndex]
                    encrypted += charLowEncrypt
                else:
                    alphaIndex = upperAlpha.find(plaintext[i])
                    upKeyIndex = alphaIndex
                    charEncrypt = self.__key[upKeyIndex].upper()
                    encrypted += charEncrypt
        return encrypted

    def decryptText(self, ciphertext):
        """Return the ciphertext decrypted with respect to the stored
        key."""
        decrypted = ""
        for i in range(len(ciphertext)):
            if ciphertext[i] == " ":
                decrypted += " "
            elif ciphertext[i] == "!":
                decrypted += "!"
            elif ciphertext[i] == "?":
                decrypted += "?"
            elif ciphertext[i] == ".":
                decrypted += "."
            elif ciphertext[i] == ",":
                decrypted += ","
            else:
                if ciphertext[i].islower() == True:
                    lowKeyIndex = self.__key.find(ciphertext[i])
                    alphaIndex = lowKeyIndex
                    charLowDecrypt = alphaLetters[alphaIndex]
                    decrypted += charLowDecrypt
                else:
                    keyIndex = self.__key.upper().find(ciphertext[i])
                    alphaIndex = keyIndex
                    charUpDecrypt = upperAlpha[alphaIndex]
                    decrypted += charUpDecrypt
        return decrypted


def main():
    cipher = SubstitutionCipher()
    while (True):
        command = input(
            ("Enter a command (getKey, changeKey, encrypt, decrypt, quit): "))
        lowerCommand = command.lower()
        if lowerCommand == "quit":
            print("Thanks for visiting!")
            break
        elif lowerCommand == "getkey":
            print("  Current cipher key: ", cipher.getKey())
        elif lowerCommand == "changekey":
            while (lowerCommand == "changekey"):
                testNewKey = input(
                    "  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")
                if testNewKey == "quit":
                    break
                elif testNewKey == "random":
                    testNewKey = makeRandomKey()
                    cipher.setKey(testNewKey)
                    print("    New cipher key: " + testNewKey)
                    break
                else:
                    if isLegalKey(testNewKey) is True:
                        cipher.setKey(testNewKey)
                        print("    New cipher key: " + testNewKey)
                        break
                    else:
                        print("    Illegal key entered. Try again!")
        elif lowerCommand == "encrypt":
            plaintext = input("  Enter a text to encrypt: ")
            encryptedtext = cipher.encryptText(plaintext)
            print("    The encrypted text is: " + encryptedtext)
        elif lowerCommand == "decrypt":
            ciphertext = input("  Enter a text to decrypt: ")
            decryptedtext = cipher.decryptText(ciphertext)
            print("    The decrypted text is: " + decryptedtext)
        elif (
                lowerCommand != "quit" or lowerCommand != "changekey" or lowerCommand != "getkey" or lowerCommand != "encrypt" or lowerCommand != "decrypt"):
            print("  Command not recognized. Try again!")


main()
