class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Find the middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge the two halves
        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2