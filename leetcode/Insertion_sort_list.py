#### Set up a suedo head for convenience. Iterate node cur throughout the list.
#### if cur.next is bigger than or equal to cur, move cur to its next
#### else: pull cur.next out of the list and iterate it from the beginning until a proper position.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        suedoHead = ListNode(-9999,head)
        cur = suedoHead
        while cur.next:
            if cur.next.val >= cur.val:
                cur = cur.next
            else:
                insert = cur.next
                cur.next = cur.next.next
                insert_pos = suedoHead
                while insert_pos.next.val < insert.val:
                    insert_pos = insert_pos.next
                insert.next = insert_pos.next
                insert_pos.next = insert
        return suedoHead.next
