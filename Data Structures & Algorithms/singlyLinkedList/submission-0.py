from typing import List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(0)  # sentinel

    def count_nodes(self) -> int:
        count = 0
        cur = self.head.next
        while cur:
            count += 1
            cur = cur.next
        return count

    def get_node(self, index: int):
        cur = self.head.next
        for _ in range(index):
            if cur is None:
                return None
            cur = cur.next
        return cur

    def get(self, index: int) -> int:
        node = self.get_node(index)
        return node.data if node else -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node

    def insertTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)

    def remove(self, index: int) -> bool:
        prev = self.head
        for _ in range(index):
            if prev.next is None:
                return False
            prev = prev.next
        if prev.next is None:
            return False
        prev.next = prev.next.next
        return True

    def getValues(self) -> List[int]:
        values = []
        cur = self.head.next
        while cur:
            values.append(cur.data)
            cur = cur.next
        return values