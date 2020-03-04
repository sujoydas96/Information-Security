class Row_Trans:
    def __init__(self):
        self.key = int()
        self.key_len = int()
        self.alphabet = ["abcdefghijklmnopqrstuvwxyz"] 
        self.encrypt = ""
    
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

    def Index_of(self,character):
        for i in range(0,26):
            if character == self.alphabet[i]:
                return i
        return None 

    def Key_Index(self,character):
        for i in range(0,6):
            if character == self.key[i]:
                return i
        return None 

    def encrypt(self,message,key):
        self.key = key
        self.key_len = len(key)
        for i in range(0,len(message)):
            p = self.Index_of(message[i])
            k = self.modulo()


