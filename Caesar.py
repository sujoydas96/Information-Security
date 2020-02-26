#Program that demonstrates the Caesar Encryption 
#Displacement refers to the key of the encryption technique. Default value = 3

class Caesar:
    def __init__(self):
        self.cipher = ""
        self.text = ""
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 

    def Index_of(self,character):
        for i in range(0,26):
            if character == self.alphabet[i]:
                return i
        return None    
    
    def encrypt(self,message,displacement = 3):
        message = message.lower()
        message = message.replace(" ","")
        for i in range(0,len(message)):
            index = self.Index_of(message[i])
            if (index+displacement) >= 26:
                index = (index + displacement) - 26
            else:
                index = index + displacement
            self.cipher = self.cipher + str(self.alphabet[index])
        return self.cipher
    
    def decrypt(self,cipher,displacement = 3):
        for i in range(0,len(cipher)):
            index = self.Index_of(cipher[i])
            if (index - displacement) < 0:
                index = (index - displacement) + 26
            else:
                index = index - displacement
            self.text = self.text + str(self.alphabet[index])
        return self.text

   

instance = Caesar()
message = str(input("Enter the message here:   "))

cipher = instance.encrypt(message)
print("The generated cipher is:  " + cipher)

message = instance.decrypt(cipher)
print("The decrypted text is: " + message)