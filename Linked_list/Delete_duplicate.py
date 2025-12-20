"""
LEETCODE PROBLEM 83

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2,3,3]
Output: [1,2,3]

"""

class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next

class Solution:
    def del_duplicate(self,head):
        if not head or not head.next:
            return head
        
        head.next=self.del_duplicate(head.next)

        if head.data==head.next.data:
            return head.next
        
        else:
            return head