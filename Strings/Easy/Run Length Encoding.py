def runLengthEncoding(string):
    encodedStr = list()
    counter = 1
    lenStr = len(string)

    for idx in range(1, lenStr):
        currChar = string[idx]
        prevChar = string[idx - 1]

        if currChar != prevChar or counter == 9:
            encodedStr.append(str(counter))
            encodedStr.append(prevChar)
            counter = 0

        counter += 1

    encodedStr.append(str(counter))
    encodedStr.append(string[-1])

    return "".join(encodedStr)
