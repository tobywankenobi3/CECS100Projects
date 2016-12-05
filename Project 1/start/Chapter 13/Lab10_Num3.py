"""Cipher Encryptor and Decrypter"""

file = open('Message', 'r+')
original = file.readlines
message = file.readlines()
newmessage = ""


# Encrypt
def encrypt(type):
    if type == "caesar":
        caesar()
    elif type == "claw":
        claw()

# Decrypt
def decrypt(type):
    if type == "claw":
        claw()
    elif type == "ceasar":
        ceasar()

# Cipher Selection
def select(choice):
    run = True
    while run:
        selection = input("What's poppin Jimbo?\n- Caesar Shift\n- Claw")
        if choice == "encrypt":
            encrypt(selection)
            run = False
        if choice == "decrypt":
            decrypt(selection)
            run = False

# Display File Text - Anfernee
def display():
    print("Original Message:",message)
    if not message == original:
        print("New Message:",message)

# Enigma Creator -

# Caesar Shift Creator -
def caesar():
    print(message)

# Claw Creator - Sean/Anfernee
def claw():
    for i in message:
        if i == 'a':
            message[i] = "|"
        elif i == 'b':
            message[i] = "|\\"
        elif i == 'c':
            message[i] = "||"
        elif i == 'd':
            message[i] = "|//"
        elif i == 'e':
            message[i] = "\\"
        elif i == 'f':
            message[i] = "||\\"
        elif i == 'g':
            message[i] = "|||"
        elif i == 'h':
            message[i] = "||/"
        elif i == 'i':
            message[i] = "/"
        elif i == 'j':
            message[i] = "|\\\\"
        elif i == 'k':
            message[i] = "|\\|"
        elif i == 'l':
            message[i] = "|\\/"
        elif i == 'm':
            message[i] = "|/\\"
        elif i == 'n':
            message[i] = "|/|"
        elif i == 'o':
            message[i] = "|//"
        elif i == 'p':
            message[i] = "\\\\"
        elif i == 'q':
            message[i] = "\\|"
        elif i == 'r':
            message[i] = "\\/"
        elif i == 's':
            message[i] = "/\\"
        elif i == 't':
            message[i] = "/|"
        elif i == 'u':
            message[i] = "//"
        elif i == 'v':
            message[i] = "||\\\\"
        elif i == 'w':
            message[i] = "||//"
        elif i == 'x':
            message[i] = "|||\\"
        elif i == 'y':
            message[i] = "|||/"
        elif i == 'z':
            message[i] = "||||"

def main():
    display()
    select("encrypt")
    display()


main()
