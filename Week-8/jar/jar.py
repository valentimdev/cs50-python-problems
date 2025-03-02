class Jar:
    def __init__(self, capacity=12,size=0):
        if capacity>0:
            self.capacity=capacity
            self.size=size
        else:
            raise ValueError()
    def __str__(self):
        cookies=""
        for num in range(self.size):
            cookies+="🍪"
        return cookies
    def deposit(self, n):
        self.size+=n
        if self.size>self.capacity:
            raise ValueError()
    def withdraw(self, n):
        self.size-=n
        if self.size<0:
            raise ValueError()
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,newSize):
        self._size  = newSize
    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, newCapacity):
        self._capacity = newCapacity
def main():
    jar = Jar()
    print(jar)

main()