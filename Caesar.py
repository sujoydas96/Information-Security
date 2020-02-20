#Program that demonstrates the Caesar Encryption Method
class Caesar:
    def __init__(self):
        self.temp = ""
        self.cipher = ""

    def alphabets(self,alphabet): #lookup table
        if alphabet == "a":
            self.temp = "D"
        elif alphabet == "b":
            self.temp = "E"
        elif alphabet == "c":
            self.temp = "F"
        elif alphabet == "d":
            self.temp = "G"
        elif alphabet == "e":
            self.temp = "H"
        elif alphabet == "f":
            self.temp = "I"
        elif alphabet == "g":
            self.temp = "J"
        elif alphabet == "h":
            self.temp = "K"
        elif alphabet == "i":
            self.temp = "L"
        elif alphabet == "j":
            self.temp = "M"
        elif alphabet == "k":
            self.temp = "N"
        elif alphabet == "l":
            self.temp = "O"
        elif alphabet == "m":
            self.temp = "P"
        elif alphabet == "n":
            self.temp = "Q"
        elif alphabet == "o":
            self.temp = "R"
        elif alphabet == "p":
            self.temp = "S"
        elif alphabet == "q":
            self.temp = "T"
        elif alphabet == "r":
            self.temp = "U"
        elif alphabet == "s":
            self.temp = "V"
        elif alphabet == "t":
            self.temp = "W"
        elif alphabet == "u":
            self.temp = "X"
        elif alphabet == "v":
            self.temp = "Y"
        elif alphabet == "w":
            self.temp = "Z"
        elif alphabet == "x":
            self.temp = "A"
        elif alphabet == "y":
            self.temp = "B"
        elif alphabet == "z":
            self.temp = "C"
        elif alphabet == " ":
            self.temp = " "
        else:
            self.temp = ""

    def encrypt(self,message):
        self.message = message.lower()
        for i in range(len(message)):
            self.alphabets(self.message[i])
            self.cipher = self.cipher + self.temp

instance = Caesar()
message = str(input("Enter the message here:   "))

instance.encrypt(message)
print("The generated cipher is:  " + instance.cipher)