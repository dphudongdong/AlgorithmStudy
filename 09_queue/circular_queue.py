from typing import Optional
from itertools import chain
"""
chain的用法 它接受一个可迭代对象列表作为输入，
并返回一个迭代器
from itertools import chain
>>> a = [1, 2, 3, 4]
>>> b = ['x', 'y', 'z']
>>> for x in chain(a, b):
... print(x)
...
1
2
3
4
x
y
z

"""
class CircularQueue:

    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity + 1
        self._head = 0
        self._tail = 0
    
    def enqueue(self, item: str) -> bool:
        # 当队满时，(tail+1)%n=head
        if (self._tail + 1) % self._capacity == self._head:
            return False
        
        self._items.append(item)
        self._tail = (self._tail + 1) % self._capacity
        return True
    
    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head = (self._head + 1) % self._capacity
            return item
    
    def __repr__(self) -> str:
        #这里需要注意下 循环队列中 head是有可能小于tail的
        if self._tail >= self._head:
            return " ".join(item for item in self._items[self._head : self._tail])
        else:
            return " ".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))

if __name__ == "__main__":
    q = CircularQueue(5)
    for i in range(5):
        q.enqueue(str(i))
        print(q)
    q.dequeue()
    q.dequeue()
    q.enqueue(str(5))
    print(q)