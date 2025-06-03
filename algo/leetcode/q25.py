from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_node = None
        current_node = head
        while current_node:
            print(f'current node: {current_node.val}, last_node: {last_node.val if last_node else last_node},')
            current_node.next, current_node, last_node = last_node, current_node.next, current_node
            # next_node = current_node.next
            # current_node.next = last_node
            # last_node = current_node
            # current_node = next_node
        return last_node


s = Solution()

# node = s.reverseKGroup(head, 3)
# while node:
#     print(node.val)
#     node = node.next

head = ListNode(
    1, ListNode(
        2, ListNode(
            3, ListNode(
                4, 
            )
        )
    )
)

node = s.reverseList(head)

counter = 0
while node:
    counter += 1
    print(node.val)
    node = node.next
    if counter > 10:
        break