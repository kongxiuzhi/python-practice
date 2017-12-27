class CaesarCipher:

    def __init__(self,shift):

        encode = [None]*26
        decode = [None]*26

        for k in range(26):
            encode[k]=chr((k+shift)%26 + ord('A'))
            decode[k]=chr((k-shift)%26 + ord('A'))
        self._forward = ''.join(encode)
        self._backward = ''.join(decode)

    def encrypt(self,message):

        return self._transform(message,self._forward)
    def decrypt(self,secret):

        return self._transform(secret,self._backward)

    def _transform(self,original,code):

        mes = list(original)
        for i in range(len(mes)):
            if mes[i].isupper():
                k = ord(mes[i])-ord('A')
                mes[i] = code[k]
        return ''.join(mes)

if __name__=="__main__":

    message = "HELLO WORLD"
    c = CaesarCipher(3)
    c1 = c.encrypt(message)
    print(c1)
    c2 = c.decrypt(c1)
    print(c2)
