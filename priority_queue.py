class Empty(Exception):
    pass


class _DoubleLinkedBase:

    class _Node:

        __slots__ = '_element','_prev','_next'

        def __init__(self,e,prev,next):

            self._element=e
            self._prev = prev
            self._next = next
    def __init__(self):
        self._header = self._Node(None,None,None)
        self._tailer = self._Node(None,None,None)
        self._header._next = self._tailer
        self._tailer._prev = self._header
        self._size = 0

    def __len__(self):

        return self._size

    def is_empty(self):

        return self._size == 0

    def _insert_between(self,e,predecessor,successor):

        newest = self._Node(e,predecessor,successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1

        return  newest

    def _delete_node(self,node):

        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._pre = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

class PositionalList(_DoubleLinkedBase):

    class Position:

        def __init__(self,container,node):

            self._container = container
            self._node = node

        def element(self):

            return self._node._element

        def __eq__(self, other):

            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):

            return not (self == other)

    def _validate(self,p):

        if not isinstance(p,self.Position):
            raise TypeError("p must be proper Postion type")
        if p._container is not self:

            raise ValueError("p does not belong to this container")
        if p._node._next is None:

            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self,node):

        if node is self._header or node is self._tailer:
            return None
        else:
            return self.Position(self,node)

    def first(self):

        return self._make_position(self._header._next)

    def last(self):

        return self._make_position(self._tailer._prev)

    def before(self,p):
        node = self._validate(p)

        return self._make_position(node._prev)

    def after(self,p):

        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):

        cursor = self.first()
        while cursor is not None:
            yield cursor
            cursor = self.after(cursor)

    def _insert_between(self,e,predecessor,successor):

        node = super()._insert_between(e,predecessor,successor)
        return self._make_position(node)

    def add_first(self,e):

        return self._insert_between(e,self._header,self._header._next)

    def add_last(self,e):

        return self._insert_between(e,self._tailer._prev,self._tailer)

    def _add_before(self,p,e):

        original = self._validate(p)
        return self._insert_between(e,original._prev,original)

    def _add_after(self,p,e):

        original = self._validate(p)
        return self._insert_between(e,original,original._next)
    def delete(self,p):

        original = self._validate(p)
        return self._delete_node(original)

    def replace(self,p,e):

        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value






class PriorityQueueBase:

    class _Item:

        __slots__ = '_key','_value'

        def __init__(self,k,v):

            self._key = k
            self._value = v
        def __lt__(self, other):

            return self._key < other._key

    def is_empty(self):

        return len(self) == 0

class UnsortedPriorityQueue(PriorityQueueBase):

    def _find_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small
    def __init__(self):

        self._data = PositionalList()

    def __len__(self):

        return len(self._data)
    def add(self,key,value):

        self._data.add_last(self._Item(key,value))

    def min(self):

        p = self._find_min()
        item = p.element()
        return (item._key,item._value)

    def remove_min(self):

        p = self._find_min()
        item = self._data.delete(p)
        return (item._key,item._value)

class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):

        return len(self._data)

    def add(self,key,value):

        newest = self._Item(key,value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data._add_after(walk,newest)

    def min(self):

        if self.is_empty():
            raise Empty("Priority queue is empty.")
        p = self._data.first()
        item = p.element()
        return (item._key,item._value)

    def remove_min(self):

        if self.is_empty():
            raise Empty("priority queue is empty")
        item = self._data.delete(self._data.first())
        return (item._key, item._value)

if __name__ == "__main__":

    p = UnsortedPriorityQueue()
    p.add(1,2)
    p.add(2,2)
    print(p.min())
    p1 = SortedPriorityQueue()
    p1.add(2,3)
    p1.add(1,5)
    print(p1.min())















