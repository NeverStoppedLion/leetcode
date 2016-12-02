# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        sums = 0
        t = 0
        q = res
        while (l1 != None or l2 != None):
            val1 = 0
            val2 = 0
            if(l1 != None):
                val1 = l1.val
                l1 = l1.next
            if(l2 != None):
                val2 = l2.val
                l2 = l2.next
            (sums, t) = self.addThree(val1, val2, t)
            p = ListNode(sums)
            q.next = p
            q = p
        
        if(t != 0):
            p = ListNode(t)
            q.next = p
        return res.next
    
    def addThree(self, num1, num2, t):
        sums = num1 + num2 + t
        return (sums % 10, sums // 10)

if (__name__ == "__main__"):
    l1 = ListNode(5)
    l2 = ListNode(7)
    solution = Solution()
    r = solution.addTwoNumbers(l1, l2)
    print r.val
    
