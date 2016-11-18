class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

    def insert(self, head, data):
        # Complete this method
        current = head
        if head is None:
            node = Node(data)
            node.next = None
            return node
        else :
            previous = head
            while current:
                previous = current
                current = current.next
            node = Node(data)
            previous.next = node
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head)