'''
    使用数组实现队列
'''
class ArrayQueue:
    
    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        #入队列的时候需要看队列的tail是否在最后 如果在最后 但是head没在0 说明还没有满
        #这个时候可以把整个队列整体移动下 这样就能腾出空间来加入新的数据
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            else:
                for i in range(0, self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0
        
        self._items.insert(self._tail, item)
        #上面这行是不是也可以换成self._items.append(item)
        self._tail += 1
        return True
    
    def enqueue1(self, item):
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            
            self._items[0 : self._tail - self._head] = self._items[self._head : self._tail]
            self._tail -= self._head
            self._head = 0
        
        if self._tail == len(self._items):
            self._items.append(item)
        else:
            self._items[self._tail] = item
        self._tail += 1
        return True

    def dequeue(self):
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            return None
    
    def __repr__(self) -> str:
        return " ".join(item for item in self._items[self._head : self._tail])

if __name__ == "__main__":
    q = ArrayQueue(10)
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("7")
    q.enqueue("8")
    print(q)