'''
LEETCODE PROBLEM 21

You are given the heads of two sorted linked lists list1 and list2.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

'''

class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next

class Solution:
    def MergeSortedLL(self,list1,list2):
        if not list1 or not list2:
            return list1 or list2
        
        if list1.data<=list2.data:
            list1.next= self.MergeSortedLL(list1.next,list2)
            return list1
        
        else:
            list2.next= self.MergeSortedLL(list2.next,list1)
            return list2