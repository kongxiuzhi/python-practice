class Empty(Exception):
    pass

class LinkedQueue:

    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,e,next):

            self._element = e
            self._next = next

    def __init__(self):

        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):

        return  self._size

    def is_empty(self):

        return self._size==0

    def first(self):

        if self.is_empty():
            raise Empty("the queue is empty")
        return self._head._element

    def last(self):

        if self.is_empty():
            raise Empty("the queue is empty")
        return self._tail._element

    def dequeue(self):

        if self.is_empty():
            raise Empty("the queue is empty")
        answer = self._head._element
        self._head=self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    def enqueue(self,e):

        newest = self._Node(e,None)
        if self.is_empty():
            self._head=newest
        else:
            self._tail._next=newest
        self._tail=newest
        self._size +=1

if __name__=="__main__":

    q1 = LinkedQueue()
    q1.enqueue(3)
    q1.enqueue(2)
    print(q1.dequeue())
    print(q1.dequeue())

