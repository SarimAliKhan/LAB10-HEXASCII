def HexASCII(alphabet):
    x = 0
    for i in range(len(alphabet)):
        x += ord(alphabet[i])*2**(16 * (len(alphabet)- i - 1))
    return x

print(HexASCII("A"))
