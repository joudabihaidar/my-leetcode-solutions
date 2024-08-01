# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Creating a new linked list called arr
        arr=ListNode()
        current=arr
        while list1!=None and list2!=None:
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next

        # add the remaining elements of the sorted lists
        if list1:
            current.next=list1
        else:
            current.next=list2
        return arr.next
        