from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lists = nums1 + nums2
        somma, l = 0, len(lists)
        for n in lists:
            somma += n
        
        return somma/l

def main():
    map_sol= Solution()
    print(map_sol.findMedianSortedArrays([1,3], [2]))
    print(map_sol.findMedianSortedArrays([1,2], [3,4]))
    print(map_sol.findMedianSortedArrays([0,0], [0,0]))
    print(map_sol.findMedianSortedArrays([], [1]))
    print(map_sol.findMedianSortedArrays([2], []))

if __name__ == "__main__":
    main()