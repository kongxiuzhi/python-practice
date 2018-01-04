def count_words(filename):
    frep ={}
    for piece in open(filename).read().lower().split():
        word = "".join(c for c in piece if c.isalpha())
        if word:
            frep[word]= 1+frep.get(word,0)

    max_word = ''
    max_count = 0
    for key,value in frep.items():
        if value > max_count:
            max_count = value
            max_word = key

    print(max_word)
    print(max_count)

from collections import MutableMapping

class MapBase(MutableMapping):

    class _Item:

        __slots__ = '_key','_value'

        def __init__(self,k,v):
            self._value = v
            self._key = k

        def __eq__(self, other):
            return self._key == other._key
        def __ne__(self, other):

            return not (self==other)
        def __lt__(self, other):

            return self._key < other._key

class UnsortedTableMap(MapBase):

    def __init__(self):

        self._table = []

    def __getitem__(self, k):

        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, k,v):

        for item in self._table:
            if item._key == k:
                item._value = v # object mutable,yinyong
                return
        self._table.append(self._Item(k,v))

    def __delitem__(self, key):

        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key Error: '+repr(k))

    def __len__(self):

        return len(self._table)
    def __iter__(self):

        for item in self._table:
            yield item._key




if __name__ == "__main__":

    u1 = UnsortedTableMap()
    u1[1] = 1
















