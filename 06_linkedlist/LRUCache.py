#https://leetcode-cn.com/problems/lru-cache/submissions/
#LRU 缓存 
#solution: 主要就是判断 新来的缓存是否存在key中 如果存在的话就把key放置在最前面
#如果新put之后 cap大于阈值 则需要将最老的缓存给删掉

class DbListNode:
    def __init__(self, x,y):
        self.key = x
        self.val = y 
        self.pre = None 
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hkeys = {}
        self.top = DbListNode(None, -1)
        self.tail =DbListNode(None, -1)
        self.top.next = self.tail
        self.tail.pre = self.top

    def node_used_react(self,node):
        #跳出原来的位置
        node.pre.next = node.next
        node.next.pre = node.pre
        #将cur移到最前面 也就是在top和top的next之间加个cur
        self.move_node_to_top(node)

    def move_node_to_top(self, node):
        top_node = self.top.next
        self.top.next = node
        node.pre = self.top
        node.next = top_node
        top_node.pre = node

    def get(self, key: int) -> int:
        if key in self.hkeys:
            cur = self.hkeys[key]
            self.node_used_react(cur)
            return self.hkeys[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.val = value
            self.node_used_react(cur)
        else:
            cur = DbListNode(key, value)
            self.hkeys[key] = cur
            self.move_node_to_top(cur)
            if len(self.hkeys.keys()) > self.cap:
                self.hkeys.pop(self.tail.pre.key)
                # 去掉原尾结点
                self.tail.pre.pre.next = self.tail
                self.tail.pre = self.tail.pre.pre



if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.hkeys)
    print(222222)
    print(cache.get(1))  # 返回  1