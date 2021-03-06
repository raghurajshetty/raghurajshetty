"""
This implementation has following stats
    Runtime -> 225ms
    Mempory -> 14.1 MB
Note - Using standard libraries
"""
from heapq import merge
from statistics import median

class Solution_heapq:
    def srm_heapq(self, nums1: list[int], nums2: list[int]) -> float:
        return median(list(merge(nums1, nums2)))
