#翻转链表 https://leetcode-cn.com/problems/reverse-linked-list/
#链表中是否有环  https://leetcode-cn.com/problems/linked-list-cycle/
#两个有序链表合并 https://leetcode-cn.com/problems/merge-two-sorted-lists/
# 删除链表倒数第n个结点 https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
# 链表的中间结点 https://leetcode-cn.com/problems/middle-of-the-linked-list/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #需要做异常点判断 
        # 如果链表为空时，代码是否能正常工作？如果链表只包含一个结点时，代码是否能正常工作？
        # 如果链表只包含两个结点时，代码是否能正常工作？代码逻辑在处理头结点和尾结点的时候，是否能正常工作？
        if head is None or head.next is None:
            return head
        prev, cur= None, head
        # 这里可以从当前开始 不从next开始 从next开始的话next.next为空就不好判断了
        # 但是判断cur的话 如果cur不为空的话 就可以继续翻转
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur 
            cur = next
        return prev

    def hasCycle1(self, head):
        """
            使用一个额外的数据结构hash_map 来遍历这个表即可
        """
        hash_map = set()
        while head:
            if head in hash_map:
                return True
            hash_map.add(head)
            head = head.next
        return False 
    
    def hasCycle(self, head):
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True 
        return False

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            采用递归的方式进行两个有序链表的合并
            我们可以如下递归地定义两个链表里的 merge 操作
            list1[0] +merge(list1[1:],list2) list1[0]<list2[0]
            list2[0] +merge(list1,list2[1:]) otherwise

        '''
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
             迭代的方式 每次找到最小的 直到l1为空或者l2为空为止
             采用哨兵的方式 构造了一个初始的列表
             等全部合并完成之后 只需要返回哨兵的next 就是排序好的链表的head
        '''
        prehead = ListNode(-1)
        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next            
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = list1 if list1 is not None else list2

        return prehead.next

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        '''
            删除倒数第N个结点
            方法1：计算出当前一共有多少个结点 得到链表的长度 L。
            随后我们再从头节点开始对链表进行一次遍历，当遍历到第 L-n+1L−n+1 个节点时，它就是我们需要删除的节点。
        '''
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for _ in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        '''
            删除倒数第N个结点
            方法2：可以使用栈 先把所有结点放进一个栈里面 然后再往外拿
            拿出的第N个就是要删除的
        '''
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy
        #这里特别需要注意 需要使用哨兵模式 这个可以很好解决只有一个结点然后删除一个结点的情况
        #在只有一个结点的情况下 stack pop完之后还有一个dummy结点
        # 它的next 就是那一个结点 next.next为None  这样在执行prev.next = prev.next.next
        # 就会把那一个结点过滤掉
        while cur:
            stack.append(cur)
            cur = cur.next
        
        for i in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        '''
            使用双指针 一个指向结尾的时候 另一个刚好指向要删除的结点的前一个
            这样就可以把那个要删除的结点过滤掉
        '''
        dummy = ListNode(0, head)
        first = second = dummy
        for _ in range(n):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

    def middleNode1(self, head: ListNode) -> ListNode:
        '''
            求链表中间结点的值
            将链表所有数据加入一个list 中间的值即使所求
            // 返回商的整数部分（向下取整）
        '''
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        return node_list[len(node_list)//2]
    
    def middleNode(self, head: ListNode) -> ListNode:
        '''
            使用快慢指针
        '''
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
