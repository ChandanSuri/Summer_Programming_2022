def caesarCipherEncryptor(string, key):
    encryptedStr = list()
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    key = key % len(alphabets)

    for alphabet in string:
        idx = alphabets.index(alphabet)
        newCharIdx = (idx + key) % len(alphabets)
        encryptedStr.append(alphabets[newCharIdx])

    return "".join(encryptedStr)
