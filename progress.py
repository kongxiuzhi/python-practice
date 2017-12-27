class Progression:

    def __init__(self,start=0):

        self._current = start

    def _advance(self):
        self._current +=1

    def __next__(self):

        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    def __iter__(self):
        return selfxik
    def print_progression(self,n):
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    def __init__(self,increment=1,start=0):

        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment

class GeometricProgression(Progression):
    def __init__(self,base=2,start=1):
        super().__init__(start)
        self._base = base
    def _advance(self):
        self._current *= self._base

class FibonacciProgression(Progression):
    def __init__(self,first=0,second=1):
        super().__init__(first)
        self._pre = second - first
    def _advance(self):

        middle = self._current + self._pre
        self._current,self._pre= middle,self._current


if __name__ == "__main__":
    p1 = Progression(1)
    p1.print_progression(10)
    p2 = ArithmeticProgression(4,1)
    p2.print_progression(10)
    p3 = GeometricProgression()
    p3.print_progression(10)
    p4 = FibonacciProgression()
    p4.print_progression(10)