import random
import operator


# Create random bytes
def randomBytes(size):
    bytes = []
    for x in range(size):
        bytes.append(random.randrange(0, 255))
    return bytes


def display(bytes):
    print("-" * 20)
    for index, item in enumerate(bytes, start=1):
        print(f'{index} = {item} ({hex(item)})')
    print("-" * 20)


def writeBytes(filename,bytes):
    with open(filename,'wb') as file:
        for i in bytes:
            file.write(i.to_bytes(1,byteorder='big'))

def readBytes(filename):
    bytes = []
    with open(filename,'rb') as file:
        while True:
            b= file.read(1) # Reading one byte
            if not b:
                break
            bytes.append(int.from_bytes(b,byteorder='big'))
    return bytes

outbytes= randomBytes(10)
display(outbytes)

# WriteBytes
filename = 'test.txt'
writeBytes(filename,outbytes)

display(readBytes(filename))




