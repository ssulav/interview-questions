"""
https://leetcode.com/problems/median-of-two-sorted-arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""

from typing import List

class mySolution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        new = []
        while nums1 and nums2:
            if nums1[i] > nums2[j]:
                new.append(nums2[j])
                del nums2[j]
                if not nums2:
                    break
            else:
                new.append(nums1[i])
                del nums1[i]
                if not nums1:
                    break
        if nums1:
            new.extend(nums1)
        if nums2:
            new.extend(nums2)
        # print(new)
        median = new[len(new)//2] if len(new) % 2 == 1 else (new[len(new)//2] + new[len(new)//2 - 1]) / 2
        # print(median)
        return median
        # return new


nums1 = [1,2,3,5,6,9]
nums2 = [3,4,5,7]

a = mySolution()
a.findMedianSortedArrays(nums1, nums2)




