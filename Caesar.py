#Program that demonstrates the Caesar Encryption 
#Displacement refers to the key of the encryption technique. Default value = 3

class Caesar:
    def __init__(self):
        self.cipher = ""
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 

    def Index_of(self,character):
        for i in range(0,26):
            if character == self.alphabet[i]:
                return i
    
    def encrypt(self,message,displacement = 3):
        message = message.lower()
        message = message.replace(" ","")
        print(message)
        for i in range(0,len(message)):
            index = self.Index_of(message[i])
            if (index+displacement) >= 26:
                index = (index + displacement) - 26
            else:
                index = int(index) + displacement
            self.cipher = self.cipher + str(self.alphabet[index])
   

instance = Caesar()
message = str(input("Enter the message here:   "))

instance.encrypt(message)
print("The generated cipher is:  " + instance.cipher)