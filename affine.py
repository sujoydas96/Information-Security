class AffineCipher:
    def __init__(self):
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
        self.cipher = ""
        self.message = ""

    def Index_of(self,character):
        for i in range(0,26):
            if character == self.alphabet[i]:
                return i 

    def modulo(self,a,b,c):    #performs a.exp(b) mod c
        if b == 0:
            return 1
        elif b%2 == 0:
            value = self.modulo(a,b/2,c)
            return (value*value)%c
        else:
            x = a%c
            y = self.modulo(a,b-1,c)
            return (x*y) % c
    
    def mul(self,p,k,mod):
        return self.modulo((p*k),1,mod)
    
    def add(self,t,k,mod):
        return self.modulo((t+k),1,mod)

    def encrypt(self,message,key1,key2):
        message = message.lower()
        message = message.replace(" ","")
        for i in range(len(message)):
            index = self.Index_of(message[i]) 
            index = self.add(self.mul(index,key1,26),key2,26)   
            if index > 26:
                index = index - 26    
            self.cipher = self.cipher + self.alphabet[index]
        return self.cipher


key1 = int(input("Enter First Key: "))
key2 = int(input("Enter Second Key: "))
message = str(input("Enter the message here: "))

instance = AffineCipher()
cipher = instance.encrypt(message,key1,key2)
print("The generated cipher text is : " + cipher)
