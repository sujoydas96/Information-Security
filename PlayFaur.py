
class PlayFair:
    def __init__(self,keyword):
        self.keyword = keyword
        self.keyword = self.keyword.lower()
        self.keyword = self.keyword.replace(" ","")

        self.arr = self.mat_create(5,5)      #matrix creation

        self.a = 0                      #temporary variables
        self.flag = 0
        
        self.alphabet = list("abcdefghijklmnopqrstuvwxyz") #removnig
        self.alphabet.reverse()
        for i in self.keyword:
            if i in self.alphabet:
                self.alphabet.remove(i) 
        
        for i in range(0,5):            #insertion of the keyword into the matrix
            for j in range(0,5):
                self.arr[i][j] = self.keyword[self.a]
                self.a += 1
                if(j > 4):
                    break
                elif(self.a >= len(self.keyword)):
                    self.flag = 1
                    break   
            if self.flag == 1:
                self.flag = 0
                j += 1
                break
        
        if 'i' in self.alphabet and 'j' in self.alphabet:            #resolving i and j
            self.alphabet.remove('j')
        elif 'i' not in self.alphabet and 'j' in self.alphabet:
            self.alphabet.remove('j')
        elif 'j' not in self.alphabet and 'i' in self.alphabet:
            self.alphabet.remove('i')
            self.flag = 1
        elif 'i' in self.alphabet and 'j' in self.alphabet:
            print("Error! (Choose a key that does not have i and j together)")
                             
        for i in range(0,5):                   #character insertions
            for j in range(0,5):
                if self.arr[i][j] == 0:
                    self.arr[i][j] = self.alphabet.pop()

    def mat_create(self,rows,cols):
        return [[0 for i in range(cols)] for j in range(rows)]
    
    def print_matrix(self):
        for rows in self.arr:
            print(rows)

    def encryption(self,word):      #return string
        word = word.replace(" ","")
        word = word.lower()
        word = list(word)
        self.i = 0
        self.j = 0
        self.k = 0
        self.l = 0
        temp = 0
        letter = "0"
        cipher = list()

        self.a = 0 
        for i in range(len(word)-1):       #counter
            if word[i] == word[i+1]:
                self.a += 1
        
        for i in range(len(word) + self.a - 1):
            if word[i] == word[i+1]:
                word.insert(i+1,"x")

        if len(word)%2 == 1:               #counter for odd even numbers
            word.append("x")

        word.reverse()

        for num in range(int(len(word)/2)):
            letter = word.pop()

            for i in range(5):
                for j in range(5):
                    if self.arr[i][j] == letter:
                        self.i = i
                        self.j = j
                        break
            
            letter = word.pop()

            for k in range(5):
                for l in range(5):
                    if self.arr[k][l] == letter:
                        self.k = k
                        self.l = l
                        break

            if self.j == self.l and self.i != self.k:                   #same column
                self.i += 1
                self.k += 1
                if self.i == 5:
                    self.i -= 5
                elif self.k == 5:
                    self.k -= 5
                cipher.append(self.arr[self.i][self.j])
                cipher.append(self.arr[self.k][self.l])

            elif self.i == self.k and self.j != self.l:                  #same row
                self.j += 1
                self.l += 1
                if self.j == 5:
                    self.j -= 5
                elif self.l == 5:
                    self.l -= 5
                cipher.append(self.arr[self.i][self.j])
                cipher.append(self.arr[self.k][self.l])

            else:
                temp = self.j
                self.j = self.l
                self.l = temp
                cipher.append(self.arr[self.i][self.j])
                cipher.append(self.arr[self.k][self.l])

        return("".join(cipher))          #return a string not a list
    
    def decrypt(self,cipher):                            #not operational
        cipher = cipher.replace(" ","")
        cipher = cipher.lower()
        cipher = list(cipher)
        self.i = 0
        self.j = 0
        self.k = 0
        self.l = 0
        temp = 0
        letter = "0"
        message = list()


   
instance = PlayFair("monarchy")
print(instance.encryption("say your angels"))
