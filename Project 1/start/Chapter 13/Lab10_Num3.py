"""Cipher Encryptor and Decrypter"""

file = open('Message', 'r+')
original = file.readlines
message = file.readlines()
newmessage = ""


# Encrypt
def encrypt():
    print("unfinished")

# Decrypt
def decrypt():
    print("unfinished")

# Cipher Selection
def select(choice):
    run = True
    while run:
        selection = input("What's poppin Jimbo?")
        if choice == "encrypt":

        if choice == "decrypt":


# Display File Text - Anfernee
def display():
    print("Original Message: "+message)
    if not message == original:
        print("New Message: "+message)

# Enigma Creator -

# Caesar Shift Creator -
def caesar():
    print(message)

# Claw Creator - Sean/Anfernee
def claw():
    for letter in message:
        if letter == 'a':
            letter = "|"
        elif letter == 'b':
            letter = "|\\"
        elif letter == 'c':
            letter = "||"
        elif letter == 'd':
            letter = "|//"
        elif letter == 'e':
            letter = "\\"
        elif letter == 'f':
            letter = "||\\"
        elif letter == 'g':
            letter = "|||"
        elif letter == 'h':
            letter = "||/"
        elif letter == 'i':
            letter = "/"
        elif letter == 'j':
            letter = "|\\\\"
        elif letter == 'k':
            letter = "|\\|"
        elif letter == 'l':
            letter = "|\\/"
        elif letter == 'm':
            letter = "|/\\"
        elif letter == 'n':
            letter = "|/|"
        elif letter == 'o':
            letter = "|//"
        elif letter == 'p':
            letter = "\\\\"
        elif letter == 'q':
            letter = "\\|"
        elif letter == 'r':
            letter = "\\/"
        elif letter == 's':
            letter = "/\\"
        elif letter == 't':
            letter = "/|"
        elif letter == 'u':
            letter = "//"
        elif letter == 'v':
            letter = "||\\\\"
        elif letter == 'w':
            letter = "||//"
        elif letter == 'x':
            letter = "|||\\"
        elif letter == 'y':
            letter = "|||/"
        elif letter == 'z':
            letter = "||||"

def main():
    print("Shite")
    caesar()


main()