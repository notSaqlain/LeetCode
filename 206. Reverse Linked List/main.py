# Link: https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = None
        while head is not None:
            new_node = ListNode(head.val)
            new_node.next = reverse
            reverse = new_node
            head = head.next
        return reverse

def main():
    s = Solution()
    print(s.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))) # 4 -> 3 -> 2 -> 1

if __name__ == "__main__":
    main()