class Empty(Exception):

    pass

class ArrayStack:

    def __init__(self):

        self._data=[]

    def __len__(self):

        return len(self._data)

    def is_empty(self):

        return len(self._data)==0

    def push(self,d):

        self._data.append(d)

    def top(self):

        if self.is_empty():

            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):

        if self.is_empty():

            raise Empty("Stack is empty")
        return self._data.pop()

def is_matched(expr):

    lefty = '({['
    righty = ')}]'

    S=ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c)!=lefty.index(S.pop()):
                return False

    return S.is_empty()

def is_matched_html(raw):

    S=ArrayStack()

    j=raw.find('<')

    while j!=-1:
        k = raw.find('>',j+1)
        if k==-1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<',k+1)
    return S.is_empty()





if __name__=="__main__":

    s1 = ArrayStack()
    s1.push(1)
    s1.push(2)
    print(s1.pop())

    print(is_matched('{}'))
    print(is_matched_html('<html>hehe</html>'))