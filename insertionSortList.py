class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head.next == None:
            return head
        
        cur = head.next
        while cur != None:
            while head.next != cur:
                if head.val > cur.val:
                    
                
        
                    

    def swap(self, node, nextNode):
        temp = node.val
        node.val = nextNode.val
        nextNode.val = temp
