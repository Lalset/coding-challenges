# LeetCode Mode:
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        fic = ListNode()
        new = fic

        while list1 and list2:
            if list1.val < list2.val:
                new.next = list1
                list1 = list1.next
            else:
                new.next = list2
                list2 = list2.next
            new = new.next

        if list1:
            new.next = list1
        if list2:
            new.next = list2

        return fic.next 
    
# Local Mode: (I still haven't been able to do it)
