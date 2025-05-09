# The Caesar cipher is an ancient encryp-
# tion algorithm used by Julius Caesar. It
# encrypts letters by shifting them over by a
# certain number of places in the alphabet. We
# call the length of shift the key. For example, if the
# key is 3, then A becomes D, B becomes E, C becomes
# F, and so on. To decrypt the message, you must shift
# the encrypted letters in the opposite direction. This
# program lets the user encrypt and decrypt messages
# according to this algorithm.

CODE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    option = input("Do you want (e)ncrypt or (d)ecrypt?: ")
    if(option == 'e'):
        mode = 1
        break
    elif(option == 'd'):
        mode = 2
        break
    print("Enter 'e' or 'd' only")
    
while True:
    key = int(input("Enter the key to use: "))
    if(key > 25 or key < 0):
        print("Wrong range, only 0 to 25")
    else:
        break

# print(option)
# print(key)
print("Enter message to encrypt or decrypt: ")
msg = input('>')
msg = msg.upper()

translation = ""
for char in msg:
    if char in CODE:
        num = CODE.find(char)
        if mode == 1:
            num = num + key
        elif mode == 2:
            num = num - key
        #if num >= len(CODE):
            
    translation = translation + CODE[num]
print(translation)
        

