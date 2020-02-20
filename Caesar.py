#Program that demonstrates the Caesar Encryption Method
class Caesar:
    def __init__(self):
        self.temp = ""
        self.cipher = ""

    def alphabets(self,alphabet): #lookup table
        if alphabet == "a":
            self.temp = "d"
        if alphabet == "b":
            self.temp = "e"
        if alphabet == "c":
            self.temp = "f"
        if alphabet == "d":
            self.temp = "g"
        if alphabet == "e":
            self.temp = "h"
        if alphabet == "f":
            self.temp = "i"
        if alphabet == "g":
            self.temp = "j"
        if alphabet == "h":
            self.temp = "k"
        if alphabet == "i":
            self.temp = "l"
        if alphabet == "j":
            self.temp = "m"
        if alphabet == "k":
            self.temp = "n"
        if alphabet == "l":
            self.temp = "o"
        if alphabet == "m":
            self.temp = "p"
        if alphabet == "n":
            self.temp = "q"
        if alphabet == "o":
            self.temp = "r"
        if alphabet == "p":
            self.temp = "s"
        if alphabet == "q":
            self.temp = "t"
        if alphabet == "r":
            self.temp = "u"
        if alphabet == "s":
            self.temp = "v"
        if alphabet == "t":
            self.temp = "w"
        if alphabet == "u":
            self.temp = "x"
        if alphabet == "v":
            self.temp = "y"
        if alphabet == "w":
            self.temp = "z"
        if alphabet == "x":
            self.temp = "a"
        if alphabet == "y":
            self.temp = "b"
        if alphabet == "z":
            self.temp = "c"
        else:
            pass

    def encrypt(self,message):
        self.message = message.lower()
        for i in range(len(message)):
            self.alphabets(self.message[i])
            self.cipher = self.cipher + self.temp

instance = Caesar()
message = str(input("Enter the message here:   "))

instance.encrypt(message)
print("The generated cipher is:  " + instance.cipher)